import cv2 as cv
import urllib
import numpy as np
from google.colab.patches import cv2_imshow as cv_imshow

# Read an image
def read_image_by_url(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)
    return img

url = "https://www.clipartmax.com/png/middle/102-1026624_logo-png-without-alpha-channel.png"
url2 = 'https://images.pond5.com/venus-atmosphere-and-without-alpha-footage-056702801_iconm.jpeg'

img = read_image_by_url(url)
img2 = read_image_by_url(url2)

first_image_size = img.shape
print(first_image_size)
second_image_size = img2.shape
print(second_image_size)
second_image_height = int(first_image_size[0]*0.25)
second_image_width = int(first_image_size[1]*0.25)
print(second_image_height)
print(second_image_width)

img2_resized = img2
img2_resized = cv.resize(img2_resized, (second_image_width, second_image_height), interpolation=cv.INTER_LINEAR)
print(img2_resized.shape)

back = img.copy()
overlay = img2_resized.copy()
h, w = back.shape[:2]
print(h, w)
h1, w1 = overlay.shape[:2]
print(h1, w1)
# let store center coordinate as cx,cy
cx, cy = ((h - h1) // 2) + int(round(h1*0.7, 0)) , ((w - w1) // 2) - w1 // 2
print(cx, cy)
# use numpy indexing to place the resized image in the center of
# background image

back[cy:cy + h1, cx:cx + w1] = overlay

shifted_matrix = np.float32([[1, 0, 50], [0, 1, -50]])
shifted_image = cv.warpAffine(back, shifted_matrix, (back.shape[1], back.shape[0]))

center = (w/2, h/2)
rotation_matrix = cv.getRotationMatrix2D(center, angle=42, scale=1.2)
rotated_img1 = cv.warpAffine(shifted_image, rotation_matrix, (h, w))
print(rotated_img1.shape)

stretch_matrix = np.float32([[1.2, 0.0, 0.0], [0.0, 1.3, 0.0]])
dsize = (int(rotated_img1.shape[1]*1.3), int(rotated_img1.shape[0]*1.2))
stretched_img1 = cv.warpAffine(rotated_img1, stretch_matrix, dsize)

shifted_matrix1 = np.float32([[1, 0, 50], [0, 1, 50]])
shifted_image1 = cv.warpAffine(stretched_img1, shifted_matrix1, (stretched_img1.shape[1], stretched_img1.shape[0]))

sheared_matrix = np.float32([[1, 0.05, 0], [0.1, 1, 0]])
sheared_img = cv.warpAffine(shifted_image1, sheared_matrix, (shifted_image1.shape[1], shifted_image1.shape[0]))

center = (sheared_img.shape[1]/2, sheared_img.shape[0]/2)
rotation_matrix2 = cv.getRotationMatrix2D(center, angle=10, scale=1)
rotated_img2 = cv.warpAffine(sheared_img, rotation_matrix2, (sheared_img.shape[1], sheared_img.shape[0]))

combined_matrix = rotation_matrix2.dot(sheared_matrix).dot(shifted_matrix1).dot(stretch_matrix)
transformed_img1 = cv.warpPerspective(img, combined_matrix, (img.shape[1], img.shape[0]))

cv_imshow(transformed_img1)
#import numpy as np
#a = np.array([[1, 2, 3, 4, 5]])
#b = np.transpos([[1/2, 1, 2, 3, 4]])
#c = a/b
#print (c)

import cv2 as cv
import numpy as np
import urllib
from google.colab.patches import cv2_imshow as cv_imshow

# Function to read an image from a URL
def read_image_by_url(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)
    return img

# Load the two images from URLs
url = "https://www.clipartmax.com/png/middle/102-1026624_logo-png-without-alpha-channel.png"
url2 = 'https://images.pond5.com/venus-atmosphere-and-without-alpha-footage-056702801_iconm.jpeg'
img1 = read_image_by_url(url1)
img2 = read_image_by_url(url2)

# Display the original images
cv_imshow('Image 1', img1)
cv_imshow('Image 2', img2)

# Resize the second image to a quarter of the first image size
height, width = img1.shape[:2]
resized_img2 = cv.resize(img2, (width // 2, height // 2))

# Display the resized image
cv_imshow('Resized Image 2', resized_img2)

# Add the resized image in the center of the first image
combined_image = img1.copy()
row_offset = (height - resized_img2.shape[0]) // 2
col_offset = (width - resized_img2.shape[1]) // 2
combined_image[row_offset:row_offset+resized_img2.shape[0], col_offset:col_offset+resized_img2.shape[1]] = resized_img2

# Display the combined image
cv_imshow('Combined Image', combined_image)

# Affine transformations
# Shift the first image by 50 pixels to the right and 50 pixels up
shift_matrix = np.float32([[1, 0, 50], [0, 1, -50]])
shifted_img1 = cv.warpAffine(img1, shift_matrix, (width, height))

# Display the shifted image
cv_imshow('Shifted Image', shifted_img1)

# Rotate the first image by 42 degrees around its center and scale it by 20%
rotation_matrix = cv.getRotationMatrix2D((width/2, height/2), 42, 1.2)
rotated_img1 = cv.warpAffine(img1, rotation_matrix, (width, height))

# Display the rotated image
cv_imshow('Rotated Image', rotated_img1)

# Perspective transformations
# Stretch the first image by 20% horizontally and 30% vertically
stretch_matrix = np.float32([[1.2, 0.0, 0.0], [0.0, 1.3, 0.0]])
stretched_img1 = cv.warpPerspective(img1, stretch_matrix, (width, height))

# Display the stretched image
cv_imshow('Stretched Image', stretched_img1)

# Shift the first image by 50 pixels to the right and 50 pixels down
shift_matrix_perspective = np.float32([[1, 0, 50], [0, 1, 50]])
shifted_img1_perspective = cv.warpPerspective(img1, shift_matrix_perspective, (width, height))

# Display the perspective-shifted image
cv_imshow('Shifted Image (Perspective)', shifted_img1_perspective)

# Apply shear transformation to the first image
shear_matrix = np.float32([[1, 0.05, 0], [0.1, 1, 0]])
sheared_img1 = cv.warpAffine(img1, shear_matrix, (width, height))

# Display the sheared image
cv_imshow('Sheared Image', sheared_img1)

# Rotate the first image by 10 degrees
rotation_matrix_perspective = cv.getRotationMatrix2D((width/2, height/2), 10, 1)
rotated_img1_perspective = cv.warpAffine(img1, rotation_matrix_perspective, (width, height))

# Display the rotated image (perspective)
cv_imshow('Rotated Image (Perspective)', rotated_img1_perspective)

# Combine all transformations into one matrix and apply to the image
combined_matrix = rotation_matrix_perspective.dot(shear_matrix).dot(shift_matrix_perspective).dot(stretch_matrix)
transformed_img1 = cv.warpPerspective(img1, combined_matrix, (width, height))

# Display the final transformed image
cv_imshow('Final Transformed Image', transformed_img1)
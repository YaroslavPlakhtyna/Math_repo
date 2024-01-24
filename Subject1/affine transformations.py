import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib

########### Генерація зображення  ####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Розмір зображення
height = 100
width = 100

# Створення чорного зображення
image = np.zeros((height, width), dtype=np.uint8)

# Додавання цифри "1"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, '1', (width // 4, height // 2), font, 2, 255, 2, cv2.LINE_AA)

# Відображення та збереження зображення
plt.imshow(image, cmap='gray')
plt.title('Згенероване зображення з цифрою "1"')
plt.show()
#############################################

# Задаємо матрицю трансформації для зсуву (зсув на 10 пікселів вправо та 50 пікселів вниз)
M = np.float32([[1, 0, 10], [0, 1, 50]])

# Виконуємо афінне перетворення
result_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Показуємо оригінальне та змінене зображення
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Оригінал')
plt.subplot(122), plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)), plt.title('Зсунуте')

plt.show()
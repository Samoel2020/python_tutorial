import numpy as np
import matplotlib.pyplot as plt
import cv2
# %matplotlib inline
# Import the image
img = cv2.imread('burano.png')

print(img.shape)

# Convert the image into RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.imshow(img_rgb)

plt.subplot(122)
plt.imshow(img)

plt.show()
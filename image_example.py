import numpy as np
import matplotlib.pyplot as plt
import cv2
# Read Image
img = cv2.imread('input.jpg')
# BGR --> RGB
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# BGR --> Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Set thresholds
th_white = 210
th_black = 85
# copy original gray
mask_white = gray.copy()
mask_black = gray.copy()
# Thresholding
mask_white[mask_white<th_white] = 0
mask_black[mask_black<th_black] = 0
mask_white[mask_white>=th_white] = 255
mask_black[mask_black>=th_black] = 255
# Median Filtering (you can remove if the text is not readable)
median_white = cv2.medianBlur(mask_white,5)
median_black = cv2.medianBlur(mask_black,5)
# Mask 3 channels
mask_white_3 = np.stack([median_white, median_white, median_white], axis=2)
mask_black_3 = np.stack([median_black, median_black, median_black], axis=2)
# Masking the image(in RGB)
result1 = np.maximum(mask_white_3, RGB)
result2 = np.minimum(mask_black_3, result1)
# Visualize the results

plt.subplot(121)
plt.imshow(RGB)
plt.title("original")
plt.axis('off')

plt.subplot(122)
plt.imshow(result2)
plt.title("result")
plt.axis('off')

plt.show()
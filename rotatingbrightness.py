import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("3x3 logo.png")
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h,w)= image.shape[:2]
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,45,1.0)
rotate=cv2.warpAffine(image,M,(w,h))
rotate_rgb=cv2.cvtColor(rotate,cv2.COLOR_BGR2RGB)
plt.imshow(rotate_rgb)
plt.title("Rotated image")
plt.show()
brightness_matrix=np.ones(image.shape, dtype="uint8") * 50
bright=cv2.add(image,brightness_matrix)
bright_rgb=cv2.cvtColor(bright,cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("bright image")
plt.show()
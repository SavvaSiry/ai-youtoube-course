import cv2 as ai
import numpy as np

# Get picture
img = ai.imread('images/demon.png')

# Edit picture
img = ai.resize(img, (img.shape[0] // 2, img.shape[1] // 2))
img = ai.GaussianBlur(img, (3, 3), 0)
img = ai.cvtColor(img, ai.COLOR_RGB2GRAY)
img = ai.Canny(img, 160, 160)

kernel = np.ones((3, 3), np.uint8)
img_1 = ai.dilate(img, kernel, iterations=1)

# Show picture
ai.imshow('Result1', img)
ai.imshow('Result2', img_1)
ai.waitKey(10000)

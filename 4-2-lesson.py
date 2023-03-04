import cv2 as ai
import numpy as np


img = ai.imread('images/3.jpg')

new_image = np.zeros(img.shape, dtype='uint8')

img = ai.cvtColor(img, ai.COLOR_RGB2GRAY)
img = ai.GaussianBlur(img, (5, 5), 0)

img = ai.Canny(img, 160, 180)

con, hir = ai.findContours(img, ai.RETR_LIST, ai.CHAIN_APPROX_SIMPLE)

ai.drawContours(new_image, con, -1, (255, 255, 255), 1)

ai.imshow('Result1', new_image)
ai.imshow('Result2', img)
ai.waitKey(10000)

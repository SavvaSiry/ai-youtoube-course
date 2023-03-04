import cv2 as ai
import numpy as np


def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)
    mat = ai.getRotationMatrix2D(point, angle, 1)
    return ai.warpAffine(img_param, mat, (width, height))


def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return ai.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))


img = ai.imread('images/demon.png')
img = rotate(img, 90)
img = transform(img, 30, 50)

ai.imshow('Result', img)
ai.waitKey(5000)

# Отражение
# img = ai.flip(img, 1)

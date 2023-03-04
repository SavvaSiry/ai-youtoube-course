import cv2 as ai

img = ai.imread('images/3.jpg')
img = ai.resize(img, (img.shape[1], img.shape[0]))

# Разделяем по цветам
r, g, b = ai.split(img)
ai.imshow('res1', r)
ai.imshow('res2', g)
ai.imshow('res3', b)

# Соединяем по цветам
img = ai.merge([r, g, b])
ai.imshow('bgr', img)

ai.waitKey(5000)



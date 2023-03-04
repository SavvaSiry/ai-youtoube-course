import cv2 as ai

img = ai.imread('images/3.jpg')
img = ai.resize(img, (img.shape[1], img.shape[0]))

img1 = ai.cvtColor(img, ai.COLOR_BGR2RGB)
img2 = ai.cvtColor(img, ai.COLOR_BGR2YCrCb)
img3 = ai.cvtColor(img, ai.COLOR_BGR2HLS)
img4 = ai.cvtColor(img, ai.COLOR_BGR2HSV)
img5 = ai.cvtColor(img, ai.COLOR_BGRA2GRAY)
img6 = ai.cvtColor(img, ai.COLOR_BGR2LUV)
img7 = ai.cvtColor(img, ai.COLOR_BGR2LAB)
img8 = ai.cvtColor(img, ai.COLOR_BGR2YUV)

ai.imshow('res1', img1)
ai.imshow('res2', img2)
ai.imshow('res3', img3)
ai.imshow('res4', img4)
ai.imshow('res5', img5)
ai.imshow('res6', img6)
ai.imshow('res7', img7)
ai.imshow('res8', img8)
ai.waitKey(30000)

import cv2 as ai

img = ai.imread('images/2.jpg')
gray = ai.cvtColor(img, ai.COLOR_BGR2GRAY)

faces = ai.CascadeClassifier('faces.xml')

result = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=2)

for (x, y, w, h) in result:
    ai.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=1)

ai.imshow('Result', img)
ai.waitKey(0)

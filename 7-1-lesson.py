import cv2 as ai

cap = ai.VideoCapture("video/mens.mp4")

while True:
    success, img = cap.read()

    img = ai.cvtColor(img, ai.COLOR_BGR2GRAY)
    faces = ai.CascadeClassifier('faces.xml')

    result = faces.detectMultiScale(img, scaleFactor=1.5, minNeighbors=4)

    for (x, y, w, h) in result:
        ai.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)

    ai.imshow('Result', img)
    if ai.waitKey(1) & 0xFF == ord('q'):
        break

import cv2
import cv2 as ai
import numpy as np

image = np.zeros((300, 300, 3), dtype='uint8')

ai.rectangle(image, (50, 50), (10, 10), (255, 255, 255), thickness=cv2.FILLED)
ai.line(image, (0, image.shape[0]//2), (image.shape[1], image.shape[0]//2), (255, 255, 255), thickness=1)
ai.line(image, (image.shape[1]//2, 0), (image.shape[1]//2, image.shape[0]), (255, 255, 255), thickness=1)
ai.circle(image, (image.shape[1]//2, image.shape[0]//2), 50, (100, 100, 0), thickness=1)
ai.putText(image, 'Hello world!', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=1)
ai.imshow('Result', image)
ai.waitKey(5000)

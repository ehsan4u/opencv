# -*- coding: utf-8 -*-
import cv2 as cv
from functions import rescaleFrame
# loading image 
#img = cv.imread('img/cats/578211-gettyimages-542930526.jpg')
#cv.imshow('Cat', img)

VideoPath='video/Dog Reviews Food With Baby Puppy Tucker Taste Test 20.mp4'
# Reading Video 
capture = cv.VideoCapture(VideoPath)
while True:
    isTrue, frame = capture.read()
    resizedframe = rescaleFrame(frame, scale=0.25)
    if not isTrue:
        continue
    cv.imshow('Dog Video - Original Size', frame)
    cv.imshow('Dog Video - Small Size', resizedframe)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

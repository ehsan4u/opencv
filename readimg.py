# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:42:46 2021

@author: ehsan
"""

import cv2 as cv
from functions import rescaleFrame

# loading image 
img = cv.imread('img/cats/578211-gettyimages-542930526.jpg')
#cv.imshow('Cat', img)
img = rescaleFrame(img, scale=0.75)
cv.imshow('Cat', img)
cv.waitKey(0)



#@uthor : Sumanth Nethi
import cv2 as cv
img = cv.imread('sample.jpeg',0)
thresh = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 20)
cv.imshow('thresh', thresh)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np 
import cv2 
  

fgbg2 = cv2.createBackgroundSubtractorMOG2()
image1 = cv2.imread('bg.jpg')
cap = cv2.VideoCapture(0)

while(1): 
    

    ret, img = cap.read()
    fgmask2 = fgbg2.apply(img)
    img2 = cv2.subtract(image1, img)
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.adaptiveThreshold(img3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		cv2.THRESH_BINARY_INV,11,2)
    contours2, hierarchy2 = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image2 = cv2.drawContours(img3, contours2, -1, (0, 255, 0), 2)
    ret2,thresh3 = cv2.threshold(img3,127,255,cv2.THRESH_BINARY_INV)
    contours2, hierarchy2 = cv2.findContours(thresh3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image2 = cv2.drawContours(img3, contours2, -1, (0, 255, 0), 2)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(gray, contours, -1, (0, 255, 0), 2)
    thresh4 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,11,2)
    contours3, hierarchy3 = cv2.findContours(thresh4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image3 = cv2.drawContours(gray, contours3, -1, (0, 255, 0), 2)
    cv2.imshow('Original', img)
    cv2.imshow('Background  Subtractor', fgmask2)
    cv2.imshow('Adaptive Thresholding + Subtract Background Frame', thresh1)
    cv2.imshow('Binary Thresholding on Frames', thresh2)
    cv2.imshow('Binary Thresholding on Frames + Subtract Background Frame', thresh3)

    cv2.imshow('Contours on Binary Threshold Frames', image)
    cv2.imshow('Contours Binary Rem Bg Frame', image2)
    cv2.imshow('Contours on Adaptive Threshold Frames', image3)
    cv2.waitKey(0);     
   
    k = cv2.waitKey(30) & 0xff;
    if k == 27: 
        break
  
cap.release() 
cv2.destroyAllWindows()

import cv2 
import numpy as np 

img = cv2.imread('lowContrast.png', 0) 
  
equ = cv2.equalizeHist(img) 
  

  
# show image input vs output 
cv2.imshow('image', equ) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 

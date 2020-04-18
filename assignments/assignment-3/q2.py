import cv2;
import numpy as np;
img = cv2.imread("Fig09_5.tif",0);
cv2.imshow('bgr_image',img)
	



#erosion

a = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
erosion = cv2.erode(img,a,iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey(0) 


#dilation


b = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
dilation = cv2.dilate(img,b,iterations = 1)
cv2.imshow('dilation',dilation)
cv2.waitKey(0) 


#opening

c = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, c)
cv2.imshow('opening',opening)
cv2.waitKey(0) 




#closing

d = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, d)
cv2.imshow('closing',closing)
cv2.waitKey(0) 



img2 = cv2.imread("Fig09_7.tif",0);
cv2.imshow('bgr_image',closing)
cv2.waitKey(0) 	


#closing for fig 09_7.tif

e = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, e)
cv2.imshow('closing',closing)
cv2.waitKey(0) 

#opening for fig 09_11.tif
img3 = cv2.imread("Fig09_11.tif",0);
cv2.imshow('bgr_image',img)
cv2.waitKey(0) 

f = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
opening = cv2.morphologyEx(img3, cv2.MORPH_OPEN, f)
cv2.imshow('opening',opening)
cv2.waitKey(0)


#opening for fig 09_11.tif
img4 = cv2.imread("Fig09_16.tif",0);
cv2.imshow('bgr_image',img4)
cv2.waitKey(0) 

g = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
gradient = cv2.morphologyEx(img4, cv2.MORPH_GRADIENT, g)
cv2.imshow('gradient',gradient)
cv2.waitKey(0)






# # Rectangular Kernel
# >>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)
# # Elliptical Kernel
# >>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)
# # Cross-shaped Kernel
# >>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
# array([[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0]], dtype=uint8)
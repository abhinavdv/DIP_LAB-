
import sys
import cv2 as cv
def main(argv):

    ddepth = cv.CV_16S
    kernel_size = 3
    window_name = "Laplace"
    imageName = 'Lenna.png'
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) 

    
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    
    dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)
   
    cv.imshow(window_name, abs_dst)
    cv.waitKey(0)
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])

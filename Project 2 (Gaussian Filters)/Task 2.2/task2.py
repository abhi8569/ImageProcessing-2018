import cv2 as cv
import numpy as np
from scipy import ndimage


def image_gradient(img, kenel,img_name="img"):
    # convolve the image with gaussian kernel
    blur = ndimage.convolve(img, kernel)

    sobelx = ndimage.sobel(blur, axis=0)
    sobely = ndimage.sobel(blur, axis=1)
    cv.imshow("sobelx", sobelx/ 255)
    cv.imshow("sobely", sobely/ 255)
    # cv.imwrite(img_name + "_sobelx.jpg", np.uint8(sobelx))
    # cv.imwrite(img_name + "_sobely.jpg", np.uint8(sobely))
    
    
    gradmag = np.uint8(np.sqrt(sobelx**2 + sobely**2))
    cv.imshow("magnitude", gradmag)
    # cv.imwrite(img_name + "_gradientmagnitude.jpg", gradmag)

    # perform f(x,y) * dg(x,y)
    kernel_sobelx = ndimage.sobel(kernel, axis=0)
    img_sobelx = ndimage.convolve(img, kernel_sobelx)
    cv.imshow("sobel_kernelx",img_sobelx/255)
    # cv.imwrite(img_name + "_sobel_kernelx.jpg", np.uint8(img_sobelx))

    kernel_sobely = ndimage.sobel(kernel, axis=1)
    img_sobely = ndimage.convolve(img, kernel_sobely)

    cv.imshow("sobel_kernely", img_sobely/255)
    # cv.imwrite(img_name + "_sobel_kernely.jpg", np.uint8(img_sobely))
    gradmag_kernelsobel = np.uint8(np.sqrt(img_sobelx**2 + img_sobely**2))
    cv.imshow("gradmag_kernelsobel", gradmag_kernelsobel)
    # cv.imwrite(img_name + "_gradmag_kernelsobel.jpg", np.uint8(gradmag_kernelsobel))
    
    cv.waitKey(0)


img_bauckhage = cv.imread("./bauckhage.jpg") 
img_bauckhage = cv.cvtColor(img_bauckhage, cv.COLOR_BGR2GRAY)
img_bauckhage = np.float32(img_bauckhage)

img_clock = cv.imread("./clock.jpg")
img_clock = cv.cvtColor(img_clock, cv.COLOR_BGR2GRAY)
img_clock = np.float32(img_clock)



ksize = 5
kernelx = cv.getGaussianKernel(ksize, -1)
kernely = cv.getGaussianKernel(ksize, -1)
kernel = np.float32(kernelx @ kernely.T)

image_gradient(img_bauckhage, kernel, img_name="img_bauckhage")
image_gradient(img_clock, kernel, img_name="img_clock")

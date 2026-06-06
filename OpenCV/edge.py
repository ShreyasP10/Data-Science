import cv2
import numpy as np
image = cv2.imread("OpenCV/OIP.webp")

# guassian blur
# blurred =cv2.GaussianBlur(image, (21,21),0)

# cv2.imshow("Original Image", image)
# cv2.imshow("Blurred Image", blurred)
# cv2.waitKey(0)
# cv2.destoryAllWindows()


#median blur
# blurred=cv2.medianBlur(image,11)
# cv2.imshow("Original Image", image)
# cv2.imshow("Blurred Image", blurred)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

#Sharpening
image=cv2.imread("OpenCV\download.webp")
sharpen_kernel= np.array([
    [0,-1,0],
    [-1,6,-1],
    [0,-1,0]
])

sharpened=cv2.filter2D(image,-1,sharpen_kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destoryAllWindows()
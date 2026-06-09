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
# image=cv2.imread("OpenCV\download.webp")
# sharpen_kernel= np.array([
    # [0,-1,0],
    # [-1,6,-1],
    # [0,-1,0]
# ])

# sharpened=cv2.filter2D(image,-1,sharpen_kernel)

# cv2.imshow("Original Image", image)
# cv2.imshow("Sharpened Image", sharpened)
# cv2.waitKey(0)
# cv2.destoryAllWindows()



#edges

#canny edge detection
# image=cv2.imread("OpenCV\OIP (1).webp", cv2.IMREAD_GRAYSCALE)
# edges=cv2.Canny(image,50,60)
# cv2.imshow("Original Image", image) 
# cv2.imshow("Canny Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#thresholding
# image=cv2.imread("OpenCV\OIP (1).webp", cv2.IMREAD_GRAYSCALE)
# ret, thresh_img=cv2.threshold(image,150,255,cv2.THRESH_BINARY)
# cv2.imshow("Original Image", image)
# cv2.imshow("Thresholded Image", thresh_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#bitwise operations
# img1=np.zeros((200,200), dtype=np.uint8)
# img2=np.zeros((200,200), dtype=np.uint8)

# cv2.circle(img1,(150,150),100,255,-1)
# cv2.rectangle(img2,(100,100),(150,150),255,-1)

# bitwise_and=cv2.bitwise_and(img1,img2)
# bitwise_or=cv2.bitwise_or(img1,img2)
# bitwise_not=cv2.bitwise_not(img1,img2)

# cv2.imshow("Circle", img1)
# cv2.imshow("Rectangle", img2)
# cv2.imshow("Bitwise AND", bitwise_and)
# cv2.imshow("Bitwise OR", bitwise_or)
# cv2.imshow("Bitwise NOT", bitwise_not)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# contours
image=cv2.imread("OpenCV/red-circle.webp")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_ , thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,contours,-1,(0,255,0),4)
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
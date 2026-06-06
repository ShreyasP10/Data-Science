import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# while True:
#     ret,frame=cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
    
#     cv2.imshow('Webcam',cv2.flip(frame,1))

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("Exiting ...")
#         break

# cap.release()
# cv2.destroyAllWindows()

camera = cv2.VideoCapture(0) 

framewidth=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frameheight=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(framewidth,frameheight)
codex=cv2.VideoWriter_fourcc(*'XVID')
print(codex)
recorded=cv2.VideoWriter('recorded.avi',codex,30.0,(framewidth,frameheight))
print(recorded)
decision=input("Do you want to record the video? (y/n)")

while True:
    success,image=camera.read() 
    if not success: 
        print("Can't receive frame (stream end?). Exiting ...")
        break
 
    cv2.imshow('Webcam Live',cv2.flip(image,1))
    if decision.lower() != 'y':
        print("Exiting ...")
        camera.release()
        cv2.destroyAllWindows()
        exit()
        recorded.write(image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting ...")
        break
camera.release()
recorded.release()
cv2.destroyAllWindows()


#Image Filtering Process

#Guassian Blur
# image=cv2.imread('test.jpeg')
# blurred=cv2.GaussianBlur(image,(7,7),5)
# cv2.imshow('Original',image)
# cv2.imshow('Blurred',blurred)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

#Median Blur
# image=cv2.imread('test.jpeg')
# blurred=cv2.medianBlur(image,11)
# cv2.imshow('Original',image)
# cv2.imshow('Blurred',blurred)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#sharping
# image=cv2.imread('download.webp')

# kernel=np.array([[0,-1,0],[-1,8,-1],[0,-1,0]])
# sharped=cv2.filter2D(image,-1,kernel)
# cv2.imshow('Original',image)
# cv2.imshow('Sharped',sharped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
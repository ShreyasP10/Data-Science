from matplotlib.pyplot import imread

import cv2

i=cv2.imread('openCV/OIP.webp',-1)

# if img is not None:
#     # cv2.imshow("Windows Title", img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWinsdows()
#     status = cv2.imwrite("output.jpeg", img)
#     if status:
#         print("Image saved successfully.")
#     else:
#         print("Failed to save image.")
# else:
#     print("Image not found.")

# Display shape

# if img is not None:
#     h,w,c=img.shape
#     print(f"Height: {h}, Width: {w}, Channels: {c}")
# else:
#     print("Image not found.")

# Display grayscale conversion

# if img is not None:
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Grayscale Image",gray)
#     cv2.waitKey(0) 
#     cv2.destroyAllWindows()
# else:
#     print("Image not found.")   



# Assingenment no1

# inp=input("Enter the path of the image: ")
# img=imread(inp,-1)
# if img is not None:
#     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Grayscale Image",gray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     choice=input("Do you want to save this? yes or no?")
#     if choice is True:
#         inp=input("Enter the path to save the grayscale image: ")
#         cv2.imwrite(inp,gray)
# else:    print("Image not found.")




#Image transformation & manipulation operations

img=cv2.imread('openCV/OIP.webp')
if img is None:
    print("Image not found.")
else:
    print("load image successfully.")

#Resizing and scaling image
    # resized =cv2.resize(img,(500,500))#(w.h)
    # cv2.imshow("Original Image", img)
    # cv2.imshow("Resized Image",resized)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()

#Crop
# if img is None:
#     print("Image not found.")
# else:
#     print("Image loaded successfully.")
#     cv2.imshow("Original Image", img)
#     cropped = img[200:300, 200:300]  # Example crop coordinates
#     cv2.imshow("Cropped Image", cropped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#image rotation & flipping
# img = cv2.imread("test.jpeg", 1)
# if img is None: 
#     print("Image not found.")
# else:
#     h,w,c=img.shape
#     center=(w//2,h//2)
#     M=cv2.getRotationMatrix2D(center,180,1.0)
#     rotated=cv2.warpAffine(img,M,(w,h))
#     # print("Image loaded successfully.")
#     cv2.imshow("Original Image", img)
#     cv2.imshow("Rotated Image", rotated)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#Flipping
# img = cv2.imread("test.jpeg", 1)
# if img is None: 
#     print("Image not found.")
# else:
#     flipped_horizontal = cv2.flip(img, 1)  # Flip horizontally
#     flipped_vertical = cv2.flip(img, 0)    # Flip vertically
#     flippedboth = cv2.flip(img, -1)              # Flip both horizontally and vertically
#     print("Image loaded successfully.")
#     cv2.imshow("Original Image", img)
#     cv2.imshow("Flipped Horizontal", flipped_horizontal)    
#     cv2.imshow("Flipped Vertical", flipped_vertical)
#     cv2.imshow("Flipped Both", flippedboth)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#Drawing lines
# img = cv2.imread("test.jpeg", 1)
# if img is None:
#     print("Image not found.")   
# else:
#     h,w,c=img.shape
    
#     pt1=(50,200)
#     pt2=(200,50)
#     color=(148,255,255)
#     thickness=5

#     cv2.line(img,pt1,pt2,color,thickness)
#     print("Image loaded successfully.")
#     cv2.imshow("Line Image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#Drawing rectangles
# img = cv2.imread("test.jpeg", 1)
# if img is None:
    # print("Image not found.")
# else:
#     pt1=(200,200)
#     pt2=(4,40)
#     color=(90,255,142)

#     thickness=3
#     cv2.rectangle(img,pt1,pt2,color,thickness)
#     print("Image loaded successfully.")
#     cv2.imshow("Rectangle Image", img)
#     cv2.waitKey(0)  
#     cv2.destroyAllWindows()

#Drawing circles
# img = cv2.imread("test.jpeg", 1)
# if img is None:
#     print("Image not found.")
# else:
#     h,w=img.shape[:3-1]
#     pt1=h//2
#     pt2=w//2
#     center=(pt2,pt1)
#     radius=50
#     color=(255,123,90)
#     thickness=10
#     cv2.circle(img,center,radius,color,thickness)
#     print("Image loaded successfully.")
#     cv2.imshow("Circle Image", img)
#     cv2.waitKey(0)  
#     cv2.destroyAllWindows()

#Drawing text
# img = cv2.imread("test.jpeg", 1)    
# if img is None:
#     print("Image not found.")
# else:
#     inp=input("Enter the text to be drawn on the image: ")
#     font=cv2.FONT_HERSHEY_SIMPLEX
#     h,w=img.shape[:2]
#     org=(h//2,w//2)
#     fontScale=1
#     color=(121,202,83)
#     thickness=2
#     cv2.putText(img,inp,org,font,fontScale,color,thickness)
#     print("Image loaded successfully.")
#     cv2.imshow("Text Image", img)
#     cv2.waitKey(0)  
#     cv2.destroyAllWindows()

##Mini project
inp_img = input("Enter the path of the image: ")
img = cv2.imread(inp_img, 1)
if img is None:
    print("Image not found.")
else:   
    print("Image loaded successfully.")
    print("Choose an operation to perform:")
    print("1. Resize")
    print("2. Crop")        
    print("3. Rotate")
    print("4. Flip")
    print("5. Draw Line")
    print("6. Draw Rectangle")
    print("7. Draw Circle")
    print("8. Draw Text")
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        width = int(input("Enter the new width: "))
        height = int(input("Enter the new height: "))
        resized = cv2.resize(img, (width, height))
        cv2.imshow("Resized Image", resized)
        print("Image resized successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, resized)
            print("Image saved successfully.")
        else:
            print("Image not saved.")
    
    elif choice == 2:
        x1 = int(input("Enter the x-coordinate of the top-left corner: "))
        y1 = int(input("Enter the y-coordinate of the top-left corner: "))
        x2 = int(input("Enter the x-coordinate of the bottom-right corner: "))
        y2 = int(input("Enter the y-coordinate of the bottom-right corner: "))
        cropped = img[y1:y2, x1:x2]
        cv2.imshow("Cropped Image", cropped)
        print("Image cropped successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, cropped)
            print("Image saved successfully.")
        else:
            print("Image not saved.")

    elif choice == 3:
        angle = float(input("Enter the rotation angle (in degrees): "))
        h, w = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h))
        cv2.imshow("Rotated Image", rotated)
        print("Image rotated successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, rotated)
            print("Image saved successfully.")
        else:
            print("Image not saved.")

    elif choice == 4:
        flip_choice = input("Enter the flip mode (horizontal/vertical/both): ").lower()
        if flip_choice == "horizontal":
            flipped = cv2.flip(img, 1)
        elif flip_choice == "vertical":
            flipped = cv2.flip(img, 0)
        elif flip_choice == "both":
            flipped = cv2.flip(img, -1)
        else:
            print("Invalid flip mode.")
            flipped = None
        
        if flipped is not None:
            cv2.imshow("Flipped Image", flipped)
            print("Image flipped successfully.")
            print("Do you want to save the image? (yes/no)")
            save_choice = input().lower()
            if save_choice == "yes":
                save_path = input("Enter the path to save the image: ")
                cv2.imwrite(save_path, flipped)
                print("Image saved successfully.")
            else:
                print("Image not saved.")

    elif choice == 5:
        x1 = int(input("Enter the x-coordinate of the starting point: "))
        y1 = int(input("Enter the y-coordinate of the starting point: "))
        x2 = int(input("Enter the x-coordinate of the ending point: "))
        y2 = int(input("Enter the y-coordinate of the ending point: "))
        color = tuple(map(int, input("Enter the color (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the line: "))
        cv2.line(img, (x1, y1), (x2, y2), color, thickness)
        cv2.imshow("Line Image", img)
        print("Line drawn successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, img)
            print("Image saved successfully.")
        else:
            print("Image not saved.")

    elif choice == 6:
        x1 = int(input("Enter the x-coordinate of the top-left corner: "))
        y1 = int(input("Enter the y-coordinate of the top-left corner: "))
        x2 = int(input("Enter the x-coordinate of the bottom-right corner: "))
        y2 = int(input("Enter the y-coordinate of the bottom-right corner: "))
        color = tuple(map(int, input("Enter the color (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the rectangle: "))
        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
        cv2.imshow("Rectangle Image", img)
        print("Rectangle drawn successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, img)
            print("Image saved successfully.")
        else:
            print("Image not saved.")
    elif choice == 7:
        x = int(input("Enter the x-coordinate of the center: "))
        y = int(input("Enter the y-coordinate of the center: "))
        radius = int(input("Enter the radius of the circle: "))
        color = tuple(map(int, input("Enter the color (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the circle: "))
        cv2.circle(img, (x, y), radius, color, thickness)
        cv2.imshow("Circle Image", img)
        print("Circle drawn successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, img)
            print("Image saved successfully.")
        else:
            print("Image not saved.")

    elif choice == 8:
        text = input("Enter the text to be drawn on the image: ")
        x = int(input("Enter the x-coordinate of the bottom-left corner of the text: "))
        y = int(input("Enter the y-coordinate of the bottom-left corner of the text: "))
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = float(input("Enter the font scale: "))
        color = tuple(map(int, input("Enter the color (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the text: "))
        cv2.putText(img, text, (x, y), font, font_scale, color, thickness)
        cv2.imshow("Text Image", img)
        print("Text drawn successfully.")
        print("Do you want to save the image? (yes/no)")
        save_choice = input().lower()
        if save_choice == "yes":
            save_path = input("Enter the path to save the image: ")
            cv2.imwrite(save_path, img)
            print("Image saved successfully.")
        else:
            print("Image not saved.")

    else:
         print("Invalid choice.")



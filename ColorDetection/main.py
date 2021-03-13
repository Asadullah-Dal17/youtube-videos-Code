import cv2 as cv 
import numpy as np 
# Creating HSV color detection function 

def ColorDetection(image, Lower, Upper ):
    # Applying HSV color
    image = hsvSpace = cv.cvtColor(image,cv.COLOR_BGR2HSV)

    # creating Mask to spreate the Specific color from frame 
    mask = cv.inRange(hsvSpace, Lower, Upper)
    
    # checking white Pixels in the mask 
    numberWhitePixels = np.sum(mask==255)


    return numberWhitePixels, mask

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()

# whil    
    
    bgrBlack = np.uint8([[[0,255,0]]])
    blackHSV = cv.cvtColor(bgrBlack, cv.COLOR_BGR2HSV)
    # print(blackHSV.shape)
    lowerRange = np.array([0, 0, 0]) 
    HSVBlack = blackHSV.reshape(3)
    print(HSVBlack, "HSv", type(HSVBlack))
    print(lowerRange,"Lower", type(lowerRange))
    upperRange = np.array([70, 255, 255])
    # print(upperRange.shape )
    
    # mask = cv.inRange(hsvColour, lowerRange, upperRange)
    whitePixels, Mask = ColorDetection(frame, lowerRange, upperRange)
    
    # whitePixels = np.sum(mask==255)
    if whitePixels >1000:
        
        # BlackHSV = cv.cvtColorTwoPlane()
        # cv.colorChange()
        print(" green is there")
        cv.putText(frame, "Green is Detected ", (50,50), cv.FONT_HERSHEY_COMPLEX, 0.9, (0,255, 255), 1)

    cv.imshow("Mask", Mask) 
    cv.imshow("Frame", frame)
    key = cv.waitKey(1)
    # Press "q" to Quite to Program
    if key ==ord('q'):
        break

cv.destroyAllWindows()
cap.release()

import cv2 as cv
import numpy as np

print("You need Opencv version 4.5.1, Yours is : ", cv.__version__)

# This Code work on Opencv Version 4.5.1
cap = cv.VideoCapture("Video.mp4")
# Qr code Detector QR
QR_Detector =cv.QRCodeDetector()
BBOX =[]
while True:
    ret, frame =cap.read()
    frame = cv.resize(frame, None, fx=0.4, fy=0.4)
    if ret == False:
        break
    # frame = cv.resize(frame, None, fx=0.5, fy=0.5)
    DATA, BBOX,_ = QR_Detector.detectAndDecode(frame)
    # print(DATA)
    cv.putText(img=frame, text=f"Data: {DATA}", org=(50,50), fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255,255,0), thickness=1  )
    
    if BBOX is not None:
        X, Y=BBOX[0][0]
        
        # print(type(DATA))

        X1, Y1 = BBOX[0][3]
        X2, Y2 = BBOX[0][2]
        X3, Y3 =BBOX[0][1]
        PolyPointList=[]
        for i in range(4):
            PolyPointList.append(list(BBOX[0][i]))
        PolyPoint =np.array(PolyPointList, np.int32)
        # print(DATA)
         
        LeftPolyPoint = PolyPoint.reshape((-1, 1, 2))
        # print(PolyPoint)  

        cv.polylines(frame, [PolyPoint], True, (0,255,0), 2)
        
   
        cv.circle(frame, (X,Y), 6, (0,255,255),-1)
        cv.circle(frame, (X1,Y1), 6, (0,255,0),-1)
        cv.circle(frame, (X2, Y2), 6, (255,0,255),-1)
        cv.circle(frame, (X3, Y3), 6, (255,255,0),-1)

    cv.imshow("orginal", frame)
    Key = cv.waitKey(1)
    
    if Key==ord("q"):
        break

cv.destroyAllWindows()
    
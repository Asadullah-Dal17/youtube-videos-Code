import cv2 as cv 

QR_Scanner = cv.QRCodeDetector()

image =cv.imread("QR_Amir Khan.png")
data, bbox, region = QR_Scanner.detectAndDecode(image)
print(data)
cv.imshow('region', image)
cv.waitKey(0)
cv.destroyAllWindows()
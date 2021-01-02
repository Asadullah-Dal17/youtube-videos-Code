import cv2 as cv

# variable 
RED =0
GREEN =0
BLUE =0
ALPHA = 255
Image = cv.imread("Logo.png", cv.IMREAD_UNCHANGED)

trasn_mask = Image[:,:,3 ]==0

Image[trasn_mask]=[BLUE, GREEN, RED, ALPHA]
cv.imwrite("GB.png", Image)
print(Image.shape)
resized = cv.resize(Image, None, fx=0.5, fy=0.5)
cv.imshow('windows', resized)
cv.waitKey(0)

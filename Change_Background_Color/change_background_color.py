import cv2 as cv

# variable 
RED =255
GREEN =255
BLUE =255
ALPHA = 200
Image = cv.imread("land.png", cv.IMREAD_UNCHANGED)

trasn_mask = Image[:,:,3 ]==0

Image[trasn_mask]=[BLUE, GREEN, RED, ALPHA]
cv.imwrite("output.png", Image)
print(Image.shape)
resized = cv.resize(Image, None, fx=0.5, fy=0.5)
cv.imshow('windows', resized)
cv.waitKey(0)

import cv2 as cv


image = cv.imread('IMG_0429.jpg')
result = cv.edgePreservingFilter(
    image, flags=1, sigma_s=30, sigma_r=0.6)
cv.imshow(' ', result)
enhanced = cv.detailEnhance(image, sigma_s=180, sigma_r=0.2)
cv.imshow('e ', enhanced)
gray, color = cv.pencilSketch(image, sigma_s=12, sigma_r=0.1)
cv.imshow('gray', gray)
s = cv.stylization(image, sigma_s=60, sigma_r=0.6)
cv.imshow('ss', s)

cv.imshow('image', image)
cv.waitKey(0)

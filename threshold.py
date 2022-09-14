import cv2

horse = cv2.imread("horse.jpg")
scalePercent = 30
height, width, dim = horse.shape
SCALED_WIDTH = int(width * scalePercent / 100)
SCALED_HEIGHT = int(height * scalePercent / 100)
scaled_horse = cv2.resize(horse, (SCALED_WIDTH, SCALED_HEIGHT))
cv2.imshow("Original", scaled_horse)
grayscale = cv2.cvtColor(scaled_horse, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(grayscale, 100, 255, cv2.THRESH_BINARY)
thresholdBlur = cv2.medianBlur(mask, 15, 0)

# src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C
sketchedThreshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, 5)
sketchedThreshold2 = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 45, 5)

# Remove background
masked = cv2.bitwise_and(scaled_horse, scaled_horse, mask=mask)

maskWithBlur = cv2.medianBlur(masked, 15, 0)
cv2.imshow("After Masking", maskWithBlur)
cv2.imshow("After adaptive threshold mean operation", sketchedThreshold)
cv2.imshow("After adaptive threshold gauss operation", sketchedThreshold2)
cv2.waitKey(0)
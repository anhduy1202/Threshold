import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)
    grayScaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C
    sketchedThreshold = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 45, 10)
    sketchedThreshold2 = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 45, 10)
    cv2.imshow("Original", frame)
    cv2.imshow("Gaussian", sketchedThreshold)
    cv2.imshow("Mean", sketchedThreshold2)
    if cv2.waitKey(1) == ord('q'):
        break

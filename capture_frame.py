import cv2
import sys

print('any key for next image, "c" to capture image, "esc" to exit')

cap = cv2.VideoCapture(sys.argv[1])

while True:

    img = cap.read()[1]

    cv2.imshow('capture', img)
    key = cv2.waitKey(0)

    if key == 27:
        break

    if key == ord('c'):
        cv2.imwrite('img.png', img)

import sys
import cv2

img_path = sys.argv[1]
img = cv2.imread(img_path)
cv2.imshow('test', img)
r = cv2.selectROI(img)
print('roi:', r)
frame_h, frame_w = img.shape[:2]
roi_w, roi_h = r[2:]
ratio = (f'HEIGHT: {roi_h / frame_h:.2f} : WIDTH: {roi_w / frame_w:.2f}')
print('ratio:', ratio)

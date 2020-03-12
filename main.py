import cv2 as cv

path = 'scoreboard-data/clips/eng_death_1080.mp4'

cap = cv.VideoCapture(path)

if not cap.isOpened():
    print('nono')
    exit()

while True:

    is_frame = cap.grab()
    if not is_frame:
        print('no frames!')
        continue

    frame = cap.retrieve()[1]

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    THRESHOLD = 60
    thresh = cv.threshold(gray, THRESHOLD, 255, cv.THRESH_BINARY)[1]

    contours, hier = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    fh, fw = thresh.shape
    RATIO_W = 0.61
    RATIO_H = 0.44
    RATIO_BUFFER = 0.04
    RATIO_AREA = 0.27
    RATIO_AREA_BUFFER = 0.05
    good_c = []
    for c in contours:
        approx = cv.approxPolyDP(c, cv.arcLength(c, True)*0.02, True)

        x, y, w, h = cv.boundingRect(c)
        if RATIO_H-RATIO_BUFFER <= (h/fh) <= RATIO_H+RATIO_BUFFER \
        and RATIO_W-RATIO_BUFFER <= (w/fw) <= RATIO_W+RATIO_BUFFER \
        and RATIO_AREA-RATIO_AREA_BUFFER <= (RATIO_W*RATIO_H) <= RATIO_AREA+RATIO_AREA_BUFFER:

            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), thickness=2, lineType=cv.LINE_AA)
            good_c.append((x, y, w, h))

    cv.imshow('orig', frame)
    for i, c in enumerate(good_c):
        cv.imshow(str(i), frame[c[1]:c[1]+c[3],c[0]:c[0]+c[2]])

    key = cv.waitKey(1)

    if key == 113:
        break

cap.release()
cv.destroyAllWindows()

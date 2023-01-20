import cv2
import numpy as np

cap = cv2.VideoCapture('input.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

lower_color = np.array([0,0,0])
upper_color = np.array([255,255,255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower_color, upper_color)

mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.putText(frame, "Ball", (int(x-radius),int(y-radius)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        
        
     out.write(frame)
    with open('output.txt', 'a') as f:
        f.write(str(x) + ',' + str(y) + ',' + str(radius) + '\n')


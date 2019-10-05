import cv2, time

cam = cv2.VideoCapture(0)

check, frame = cam.read()

time.sleep(5)
cv2.imwrite("image.jpg", frame)

cam.release()


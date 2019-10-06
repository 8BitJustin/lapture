import cv2, time
from datetime import datetime

# timestamp for file name as time image saved
timestamp = datetime.now()
timestamp = timestamp.strftime("%Y-%m-%d-%H-%M-%S")

cam = cv2.VideoCapture(0)

check, frame = cam.read()

print(check)

time.sleep(3)

cv2.imwrite(timestamp + ".jpg", frame)

cam.release()

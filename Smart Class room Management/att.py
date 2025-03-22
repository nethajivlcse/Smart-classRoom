import cv2
import time

video_capture = cv2.VideoCapture(0)  
time.sleep(2)  # Allow camera to initialize

if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()

    if not ret or frame is None:
        print("Warning: Empty frame captured.")
        continue  # Skip this frame and retry

    cv2.imshow('Camera Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

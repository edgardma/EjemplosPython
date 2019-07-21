import face_recognition
import cv2
import time

video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    start_time = time.time()
    ret, frame = video_capture.read()
    fast_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = fast_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)

    for top, right, bottom, left in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)

    print("FPS: ", 1.0 / (time.time() - start_time))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import time
import os
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    min_detection_confidence=0.5) as pose:
    # upload the image from your directory for testing
    image = cv2.imread('Sample/1.jpg') 
    image_height, image_width, _  = image.shape
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imwrite(r'Sample/1.png', annotated_image)

# Webcam input:
#cap = cv2.VideoCapture(0)
# upload any testing video for training
cap = cv2.VideoCapture("testing.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# to save the output  video
out = cv2.VideoWriter('outpyq.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 20, (frame_width,frame_height))
prevTime = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime
    cv2.putText(image, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)
    out.write(image)
    cv2.imshow('BlazePose', image)
    cv2.imshow('resources/1.png', annotated_image)
    if cv2.waitKey(5) & 0xFF == ord('q'): # to quit screen
        break
cap.release()
cv2.destroyAllWindows
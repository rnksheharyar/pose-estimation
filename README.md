# pose-estimation
The model is trained on the provided video which includes 50 ways of falling body.
Using Mediapipe for body keypoints in real time but it is limited to only one user.
The frame rate is 20 frames per second
The specific model used in the code is the BlazePose model from the MediaPipe library.
It provides 33 pose landmarks represents various body joints such as shoulders, elbows, wrists, hips, knees and ankles.

Advantages:
Fast and accurate for real time and off line video.
Can be run on PC do not require GPU
donot require bigdata set for training model

cons:
Limited to only one body in the frame
More accurate on video rather than images
Before run please install these two libraries
# pip install OpenCV-Python
# pip install MediaPipe

Thank you
Sheharyar

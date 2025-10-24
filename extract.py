import cv2
import os


video_path= "input_video/input.mp4" 
frame_folder = "frames"
if not os.path.exists(frame_folder):
    os.makedirs(frame_folder)


cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
print("Extracting frames")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_filename = os.path.join(frame_folder, f"frame_{frame_count:05d}.jpg")
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames to '{frame_folder}' folder.")

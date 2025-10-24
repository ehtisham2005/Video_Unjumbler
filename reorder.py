import cv2
import os
from skimage.metrics import structural_similarity as ssim
import numpy as np


frame_folder = "frames"
ordered_folder = "ordered_frames"
output_video = "output/unjumbled_video.mp4"
fps = 30
resize_dim = (160, 90)               


for folder in [ordered_folder, "output"]:
    if not os.path.exists(folder):
        os.makedirs(folder)


frame_files = sorted([f for f in os.listdir(frame_folder) if f.endswith(".jpg")])
frames = [cv2.imread(os.path.join(frame_folder, f)) for f in frame_files]
print(f"Loaded {len(frames)} frames from '{frame_folder}'.")


gray_frames = [cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), resize_dim) for f in frames]


print("Reordering frames using greedy SSIM approach")
ordered_frames = [frames[0]]
used_indices = set([0])
current_idx = 0

while len(ordered_frames) < len(frames):
    last_gray = gray_frames[current_idx]
    max_score = -1
    next_idx = None
    print("ordering")
    

    for i, gf in enumerate(gray_frames):
        if i in used_indices:
            continue
        score = ssim(last_gray, gf)
        if score > max_score:
            max_score = score
            next_idx = i
    
    ordered_frames.append(frames[next_idx])
    used_indices.add(next_idx)
    current_idx = next_idx

print("Frame ordering complete")
ordered_frames = ordered_frames[::-1]


for idx, frame in enumerate(ordered_frames):
    cv2.imwrite(os.path.join(ordered_folder, f"frame_{idx:05d}.jpg"), frame)


height, width, _ = ordered_frames[0].shape
out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

for frame in ordered_frames:
    out.write(frame)

out.release()
print(f"Video reconstructed and saved to '{output_video}'")

import cv2
import os
from tqdm import tqdm

# === CONFIG ===
VIDEO_PATH = "sample_video.mp4"  # Replace with your video path
OUTPUT_DIR = "input_frames"
FRAME_SKIP = 1  # 1 = every frame, 2 = every 2nd frame, etc.
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === FRAME EXTRACTION ===
cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"📽️ Total frames in video: {total_frames}")

frame_num = 0
saved_count = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    if frame_num % FRAME_SKIP == 0:
        # Optional: Crop center square
        height, width, _ = frame.shape
        min_dim = min(height, width)
        start_x = (width - min_dim) // 2
        start_y = (height - min_dim) // 2
        frame_cropped = frame[start_y:start_y + min_dim, start_x:start_x + min_dim]

        # Do NOT resize — keep high resolution
        frame_filename = os.path.join(OUTPUT_DIR, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame_cropped)
        saved_count += 1

    frame_num += 1

cap.release()
print(f"✅ Extracted and saved {saved_count} high-res cropped frames to '{OUTPUT_DIR}'")

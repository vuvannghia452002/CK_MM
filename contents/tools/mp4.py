import os
import glob


root = r"../../"
mp4_files = glob.glob(os.path.join(root, "**/*.mp4"), recursive=True)

if len(mp4_files) > 0:
    for i in mp4_files:
        print("🚀 Giá trị của i:", i)
else:
    print("Không có file .mp4")

print("Xong")

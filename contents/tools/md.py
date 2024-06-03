import os
import glob


root = r"../../"
md_files = glob.glob(os.path.join(root, "**/*.md"), recursive=True)

if len(md_files) > 0:
    for i in md_files:
        print("🚀 Giá trị của i:", i)
else:
    print("Không có file .md")

print("Xong")

import os
import glob


root = r"../../"
pdf_files = glob.glob(os.path.join(root, "**/*.pdf"), recursive=True)

if len(pdf_files) > 0:
    for i in pdf_files:
        print("🚀 Giá trị của i:", i)
else:
    print("Không có file .pdf")

print("Xong")

import os
import subprocess

python_files = [file for file in os.listdir() if file.endswith('.py')]


def check_image(file):
    # return True
    if (file == "image.py"):
        print("image.py")
        exit()


for python_file in python_files:
    if python_file == "all.py":
        continue

    check_image(python_file)
    file_path = os.path.abspath(python_file)
    subprocess.call(["python", file_path])

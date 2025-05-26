import cv2
from pathlib import Path
import os

# Get the parent directory of this script
parent_dir = Path(__file__).resolve().parent

# Change current working directory to the script's parent directory
os.chdir(parent_dir)


folders = ['greyscale416', 'greyscale320']
sets = ['train', 'test', 'valid']
for folder in folders:
    for set in sets:
        set_path = os.path.join(folder,set,'images')
        images_path = os.listdir(set_path)
        images_path = [os.path.join(set_path,image_path) for image_path in images_path]
        for image_path in images_path:
            image = cv2.imread(str(image_path))
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(image_path, gray_image)

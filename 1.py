# Resize all the png files from 1000*600 to 250*150

import os
from PIL import Image
def resize_images_in_directory(directory, size=(250, 150)):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            file_path = os.path.join(directory, filename)
            with Image.open(file_path) as img:
                img = img.resize(size)
                img.save(file_path)
                print(f'Resized {filename} to {size}')
if __name__ == "__main__":
    directory = '.'  # Current directory
    for dir in os.listdir(directory):
        try:
            print(dir)
            if os.path.isdir(dir):
                resize_images_in_directory(dir)
        except Exception as e:
            print(f"Error processing directory: {dir}, Error: {e}")
            continue
from glob import glob

import numpy as np
import cv2
import sys
import os

# Get image filename from cli
images = glob('./images/*.png') + glob('./images/*.jpg')
scale = 0.25
if len(sys.argv) > 2:
    try:
        scale = float(sys.argv[2])
    except ValueError:
        print("Scaling must be a number, e.g., 0.5 or 2")
        sys.exit(1)
if len(sys.argv) > 1:
    img = sys.argv[1]
    image_src = os.path.join("./images", img)
    print(f"Using image: {image_src}, at {scale} scale")
    if not (img.endswith(".png") or img.endswith(".jpg")):
        print("Error: Only .png and .jpg files are supported.")
        sys.exit(1)
else:
    image_src = images[0]
    print(f" in else {image_src}")
    print(f"Using image: {image_src}, at {scale} scale")




# reading the image
image = cv2.imread(image_src)
if image is None:
    print(f"Error: Unable to load image '{image_src}'")
    sys.exit(1)

downsized = cv2.resize(image, None, fx=scale,fy=scale)

# setting height, width, and channels(always 3) of the image to h w c
h,w,c = downsized.shape

# creating a blank canvas filled with x in the dimensions of the downsized pic
grid = []
for i in range(h):
    grid.append([" "] * w)



for y in range(h):
    for x in range(w):
        r,g,b = downsized[y,x,0], downsized[y,x,1],  downsized[y,x,2]
        # z is brightness value
        z = (int(r) + int(g) + int(b))/3
        # brighter values are going to be given stronger characters, assuming dark mode
        if z > 230:
            grid[y][x] = "@"
        elif z > 204:
            grid[y][x] = "#"
        elif z > 179:
            grid[y][x] = "&"
        elif z > 153:
            grid[y][x] = "$"
        elif z > 128:
            grid[y][x] = "%"
        elif z > 102:
            grid[y][x] = "?"
        elif z > 77:
            grid[y][x] = "}"
        elif z > 51:
            grid[y][x] = "!"
        elif z > 26:
            grid[y][x] = "^"

if image_src.endswith(".png"):
    stripped = image_src.split("\\")
    file_path = stripped[1].replace(".png", ".txt")
else:
    stripped = image_src.split("\\")
    file_path = stripped[1].replace(".jpg", ".txt")

try:
    with open(file_path, "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")
    print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


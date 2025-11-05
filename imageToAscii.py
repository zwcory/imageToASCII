import numpy as np
import cv2

imageSrc = 'monaLisa.jpg'
image = cv2.imread(imageSrc)

# todo
# allow sizing select, and input for name of image

# downsized = cv2.resize(image, None, fx=0.05,fy=0.05)
downsized = cv2.resize(image, None, fx=0.025,fy=0.025)

# setting height, width, and channels(always 3) of the image to h w c
h,w,c = downsized.shape

# creating a blank canvas filled with x in the dimensions of the downsized pic
grid = []
for i in range(h):
    grid.append([" "] * w)



for y in range(h):
    for x in range(w):
        r,g,b = downsized[y,x,0], downsized[y,x,1],  downsized[y,x,2]
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

file_path = "text.txt"
try:
    with open(file_path, "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")
    print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

print(h,w,c)
# Shape is Height, width, rgb Layer
print(image.shape)


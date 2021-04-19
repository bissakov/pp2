from PIL import Image
import numpy as np

img = Image.open('assets/food_range_level3.png').convert('RGB')

data = np.asarray(img)

for i in range(len(data)):
    y = i
    for j in range(len(data[i])):
        x = j
        rgb = tuple(data[i][j])
        if rgb == (0,0,0):
            f = open("assets/food_range_level3.txt","a")
            f.write("Vector2(" + str(x) + "," + str(y) + "),\n")
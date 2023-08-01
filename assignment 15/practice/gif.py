import os
import imageio
import numpy as np

myfiles = os.listdir("img")

images = []
for i in range(len(myfiles)):
    image = imageio.imread("img/" + myfiles[i])
    image = np.resize(image, (700, 800, 3))
    images.append(image)
print(images)
imageio.mimsave("2.gif" , images)
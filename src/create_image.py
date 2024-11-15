from cmath import rect
from matplotlib.pylab import rec
import numpy as np
import matplotlib.pyplot as plt
from generate_random import generate_random


random_data = generate_random(103, 0, 10, True) 
print(random_data)

fig, ax = plt.subplots(figsize=(6,6))

for i in range(0, 100, 2):
    circle_center_x = random_data[i] * 10  
    circle_coordinate_y = random_data[i+1] * 10
    size = np.random.rand() * 2000 
    rectangle_center_x = random_data[i+2] * 10
    rectangle_coordinate_y = random_data[i+3] * 10
    color = np.random.rand(3,)  
    circle = plt.Circle((circle_center_x, circle_coordinate_y), size/200, color=color, alpha=0.5)  
    square = plt.Rectangle((rectangle_center_x, rectangle_coordinate_y), size/200, size/200, color=color, alpha=0.5)
    ax.add_artist(circle)
    ax.add_artist(square)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
plt.gca().set_aspect('equal', adjustable='box')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from generate_random import generate_random


random_data = generate_random(100, 0, 10, True) 
print(random_data)

fig, ax = plt.subplots(figsize=(6,6))

for i in range(0, 100, 2):
    x = random_data[i] * 10  
    y = random_data[i+1] * 10
    size = np.random.rand() * 2000 
    color = np.random.rand(3,)  
    circle = plt.Circle((x, y), size/200, color=color, alpha=0.5)  
    ax.add_artist(circle)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

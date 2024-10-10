import numpy as np
import matplotlib.pyplot as plt


random_data = np.random.rand(100)  

fig, ax = plt.subplots(figsize=(6,6))

for i in range(0, 100, 2):
    x = random_data[i] * 10  
    y = random_data[i+1] * 10
    size = np.random.rand() * 200  
    color = np.random.rand(3,)  
    circle = plt.Circle((x, y), size/200, color=color, alpha=0.5)  
    ax.add_artist(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

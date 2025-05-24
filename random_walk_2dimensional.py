#random walk 2dimensional
import numpy as np
import matplotlib.pyplot as plt

#parameters

number_steps = 1000

#Generate random steps for x and y directions:

# Each step is randomly either [-1, 0, 1] but they are not both 0 

x_steps = np.random.choice([-1, 0, 1], size=number_steps)
y_steps = np.random.choice([-1, 0, 1], size=number_steps)

mask = ~((x_steps==0) & (y_steps==0)  )

x_steps = x_steps[mask]
y_steps = y_steps[mask]

#Cumulative sum to get the position over time

x_position = np.cumsum(x_steps)
y_position = np.cumsum(y_steps)


#potting the path

plt.figure(figsize=(8,8))
plt.plot(x_position, y_position, color='blue', linewidth=1)
plt.scatter(0,0, color='green', label='start', s=50)
plt.scatter(x_position[-1], y_position[-1], color='red', label='end', s=50)

plt.title("Random Walk 2D")
plt.xlabel("X-position")
plt.ylabel("Y-position")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.axis('equal')


plt.show()
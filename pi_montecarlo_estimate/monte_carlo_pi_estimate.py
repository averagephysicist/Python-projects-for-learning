import numpy as np
import matplotlib.pyplot as plt

#number of points

N = 12000

x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

#check if pints are on the circle:

inside_circle = x**2 + y**2 <= 1

#estimate pi

pi_estimate = (np.sum(inside_circle) / N) * 4

print(f"pi estimate: {pi_estimate}")

#plot

plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='inside')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='outside')
plt.title('Monte Carlo Estimation of Pi')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.text(-1.2, -1.4, f'π ≈ {pi_estimate:.5f}', fontsize=12, color='black')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100      # Initial stock price
mu = 0.07     # Expected return (drift)
sigma = 0.25  # Volatility
T = 1         # Time horizon (1 year)
N = 252       # Number of time steps (trading days)
dt = T / N    # Time step
num_paths = 100  # Number of random paths

# Time array
time = np.linspace(0, T, N)

# Simulate paths
S_paths = np.zeros((num_paths, N))
S_paths[:, 0] = S0

for i in range(num_paths):
    random_shocks = np.random.normal(0, 1, N-1)
    W = np.cumsum(random_shocks) * np.sqrt(dt)
    drift = (mu - 0.5 * sigma**2) * time[1:]
    diffusion = sigma * W
    S_paths[i, 1:] = S0 * np.exp(drift + diffusion)

# Plotting
plt.figure(figsize=(12, 6))
for i in range(num_paths):
    plt.plot(time, S_paths[i], linewidth=0.8, alpha=0.7)

plt.title('100 Simulated Stock Price Paths (Geometric Brownian Motion)')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.grid(alpha=0.3)
plt.show()
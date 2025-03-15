# Diffusion-Limited Aggregation (DLA) fractal generator (Figure 2)
import numpy as np
import matplotlib.pyplot as plt

def generate_dla(size=500, particles=5000):
    grid = np.zeros((size, size))
    grid[size//2, size//2] = 1  # Seed particle
    # [...] Full DLA algorithm here
    return grid

# Save fractal as PNG
plt.imshow(generate_dla(), cmap='viridis')
plt.savefig('figures/DLA_fractal.png')

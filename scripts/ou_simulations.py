# Ornstein-Uhlenbeck time-field trajectories (Figure 1)
import numpy as np

def simulate_ou(alpha=0.5, beta=1.0, steps=1000):
    dt = 0.01
    T = np.zeros(steps)
    for i in range(1, steps):
        dW = np.random.normal(0, np.sqrt(dt))
        T[i] = T[i-1] - alpha*T[i-1]*dt + beta*dW
    return T

# Example usage:
T1 = simulate_ou(alpha=0.5, beta=1.0)
T2 = simulate_ou(alpha=2.0, beta=1.0)

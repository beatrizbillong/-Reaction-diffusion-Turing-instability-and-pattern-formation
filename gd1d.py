import numpy as np
import matplotlib.pyplot as plt
from gierer_meinhardt_1d import is_turing_instability  # Import your function

# Define parameter ranges for (a, d)
a_values = np.linspace(0.1, 1.5, 100)  # Range of a
d_values = np.linspace(0.1, 50, 100)  # Range of d

# Create a grid to evaluate Turing instability
A, D = np.meshgrid(a_values, d_values)
Turing_space = np.zeros_like(A, dtype=bool)

# Evaluate Turing instability for each (a, d)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        Turing_space[i, j] = is_turing_instability(
            A[i, j], b=1.0, d=D[i, j]
        )  # Fix b = 1

# Plot Turing space
plt.figure(figsize=(8, 6))
plt.contourf(A, D, Turing_space, levels=1, cmap="coolwarm", alpha=0.7)
plt.xlabel("a")
plt.ylabel("d")
plt.title("Turing Space in the Gierer-Meinhardt Model (b = 1)")
plt.colorbar(label="1 = Turing Instability")
plt.savefig("turing_space.png")  # Save the image
plt.show()

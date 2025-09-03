import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend for headless environments

import matplotlib.pyplot as plt
import numpy as np

print("✅ Matplotlib version:", matplotlib.__version__)

# Generate sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)", color="blue")
plt.title("Basic Matplotlib Test")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)

# Save to PNG
plt.savefig("test_plot.png")
print("📁 Plot saved as test_plot.png")

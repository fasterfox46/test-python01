import scipy
from scipy import linalg, optimize, stats

print("✅ SciPy version:", scipy.__version__)

# Linear algebra: solve Ax = b
A = [[3, 2], [1, 4]]
b = [6, 8]
x = linalg.solve(A, b)
print("🔢 Linear solve Ax = b:", x)

# Optimization: minimize a quadratic function
def f(x): return (x - 3)**2 + 4
result = optimize.minimize(f, x0=0)
print("📉 Optimization result:", result.x)

# Statistics: sample and describe a normal distribution
data = stats.norm.rvs(loc=0, scale=1, size=1000)
mean, std = stats.norm.fit(data)
print("📊 Fitted normal distribution: mean =", mean, ", std =", std)

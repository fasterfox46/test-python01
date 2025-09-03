import numpy as np

# Create a simple NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform a basic operation (e.g., add 10 to each element)
result_array = arr + 10

# Print the original and resulting arrays
print("Original Array:", arr)
print("Resulting Array (after adding 10):", result_array)

# Verify a basic property (e.g., shape)
print("Shape of the array:", result_array.shape)

# Perform a dot product with another array
arr2 = np.array([5, 4, 3, 2, 1])
dot_product = np.dot(arr, arr2)
print("Dot product of arr and arr2:", dot_product)

print("\nNumPy library appears to be working correctly.")

import pandas as pd

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Print the DataFrame to verify its creation
print("Original DataFrame:")
print(df)

# Access a specific column
print("\n'Age' column:")
print(df['Age'])

# Filter data based on a condition
print("\nPeople older than 30:")
print(df[df['Age'] > 30])

# Add a new column
df['Salary'] = [50000, 60000, 75000, 90000]
print("\nDataFrame with 'Salary' column:")
print(df)

# Calculate basic statistics
print("\nAverage Age:", df['Age'].mean())
print("Maximum Salary:", df['Salary'].max())

import pandas as pd

series = pd.Series([1, 2, 3], index=['A', 'B', 'C'])

# Access elements by index
print("Element at index 'A': ", series['A'])
print("Element at index 'B': ", series['B'])
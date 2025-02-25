import numpy as np

myArray = np.array([[1,2],[3,4],[5,6]])
sumArray = myArray.sum(axis=0)

print("Sum of each column: ", sumArray)
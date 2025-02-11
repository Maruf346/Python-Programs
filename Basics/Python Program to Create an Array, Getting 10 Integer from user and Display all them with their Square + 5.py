import numpy as np

numbers = []

for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

myArr = np.array(numbers)
print("Array: ", myArr)

for num in numbers:
    print(f"Square of {num} is: {num**2}")

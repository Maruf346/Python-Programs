import numpy as np

numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

array = np.array(numbers)
product = np.prod(array)

print(f"The product of the numbers {array} is: {product}")

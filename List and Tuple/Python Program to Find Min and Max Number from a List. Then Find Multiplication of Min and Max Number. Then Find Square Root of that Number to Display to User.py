import math

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
min_num = min(numbers)
max_num = max(numbers)
result = min_num * max_num
square_root = math.sqrt(result)

print("Min number:", min_num)
print("Max number:", max_num)
print("Multiplication of Min and Max:", result)
print("Square root of the result:", square_root)

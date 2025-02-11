numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

sum_of_numbers = sum(numbers)

product_of_numbers = 1
for num in numbers:
    product_of_numbers *= num

print("Numbers are:", numbers)
print("Sum of all nums:", sum_of_numbers)
print("Multiplication of all nums:", product_of_numbers)

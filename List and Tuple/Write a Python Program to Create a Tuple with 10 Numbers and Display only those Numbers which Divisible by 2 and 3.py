
nums = (10, 12, 15, 18, 20, 24, 30, 35, 36, 40)

res = [num for num in nums if num % 2 == 0 and num % 3 == 0]
print("Numbers divisible by both 2 & 3 are:", res)

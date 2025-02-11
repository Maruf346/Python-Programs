nums = []

for i in range(10):
    num = int(input("Enter number " + str(i+1)+": "))
    nums.append(num)

print("Nums less than 20 & greater than 10: ")
for num in nums:
    if num < 20 and num > 10:
        print(num)
    
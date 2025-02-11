nums = []

for i in range(10):
    num = int(input("Enter number " + str(i+1)+": "))
    nums.append(num)

print("Odd numbers are: ")
for num in nums:
    if not num%2==0:
        print(num)
    

nums = []
for i in range(5):
    nums.append(input("Enter number "+str(i+1)+": "))
print("Initial list:")
print(nums)

nums.pop(0)
print("after removing 1st element:")
print(nums)
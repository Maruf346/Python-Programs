
nums = []
for i in range(5):
    nums.append(input("Enter number "+str(i+1)+": "))

print("Initial list:")
print(nums)

square = [i*i for i in nums]
print("square of elements:")
print(square)
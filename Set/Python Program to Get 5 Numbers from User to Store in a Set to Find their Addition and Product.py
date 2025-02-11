mySet = set()

for i in range(5):
    num = int(input("Enter a num: "))
    mySet.add(num)

totSum = sum(mySet)
print("Total sum: ",totSum)

product = 1
for item in mySet:
    product *= item

print("Product: ",product)
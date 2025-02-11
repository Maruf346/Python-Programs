mySet1 = set()
mySet2 = set()

print("For set1: ")
for i in range(5):
    num = int(input("Enter a num: "))
    mySet1.add(num)

print("For set2: ")
for i in range(3):
    num = int(input("Enter a num: "))
    mySet2.add(num)

print("Set1:", mySet1)
print("Set2:", mySet2)

res = mySet2.issubset(mySet1)
print("Set1 is subset of Set2?: ", res)
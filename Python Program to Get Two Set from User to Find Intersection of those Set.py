mySet1 = set()
mySet2 = set()

print("For set1: ")
for i in range(5):
    num = int(input("Enter a num: "))
    mySet1.add(num)

print("For set2: ")
for i in range(5):
    num = int(input("Enter a num: "))
    mySet2.add(num)

print("Set1:", mySet1)
print("Set2:", mySet2)

diff = mySet1.intersection(mySet2)
print("Intersection of Set1 and Set2: ", diff)

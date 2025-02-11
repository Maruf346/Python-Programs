mySet = {"green", "university", "of"}
print("Initial set: ", mySet)

newSet = set()
for i in range(2):
    text = input("Enter a text: ")
    newSet.add(text)

mySet.update(newSet)
print("Updated set: ", mySet)
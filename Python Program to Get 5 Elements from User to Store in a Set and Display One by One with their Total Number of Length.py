mySet = set()

for i in range(5):
    text = input("Enter a text: ")
    mySet.add(text)

print("Initial set: ", mySet)

print("Lengths of Set elements: ")
for item in mySet:
    print(len(item))
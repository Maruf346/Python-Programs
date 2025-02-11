mySet = set()

for i in range(5):
    text = input("Enter a text: ")
    mySet.add(text)

print("Initial set: ", mySet)

print("Set elements in lowercase")
for item in mySet:
    print(item.lower())

print("Set elements in uppercase")
for item in mySet:
    print(item.upper())
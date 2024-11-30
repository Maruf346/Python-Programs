myList = []
mySet = set()
for i in range(5):
    text = input("Enter a text: ")
    myList.append(text)
    
print("List: ", myList)

mySet.update(myList)
print("Set: ", mySet)
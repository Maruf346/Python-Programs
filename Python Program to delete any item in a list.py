
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("Current items:")
print(items)

index = int(input("\nEnter the index of the item you want to modify: "))

if 0 <= index < len(items):
    items.pop(index)
    
    print("\nAfter Deletion: ")
    print(items)
else:
    print("Invalid index...!")

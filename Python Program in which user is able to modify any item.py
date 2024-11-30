
items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("Current items:")
print(items)

index = int(input("\nEnter the index of the item you want to modify: "))

if 0 <= index < len(items):
 
    new_item = input(f"Enter the new value for '{items[index]}': ")
    
    items[index] = new_item
    
    print("\nModified list:")
    print(items)
else:
    print("Invalid index...!")

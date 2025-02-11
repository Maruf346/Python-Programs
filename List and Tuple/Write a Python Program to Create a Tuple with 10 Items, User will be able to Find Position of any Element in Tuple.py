myTuple = (10, 12, 15, 18, 20, 24, 30, 35, 36, 40)

print("Original tuple:", myTuple)

item = int(input("Search position of: "))

addr = myTuple.index(item)
print(f"The item {item} is at {addr} no position.")

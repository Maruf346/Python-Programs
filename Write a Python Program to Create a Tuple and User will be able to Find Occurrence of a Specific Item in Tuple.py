myTuple = (1, 2, 3, 3, 2, 1, 2)

print("Original tuple:", myTuple)

item = int(input("Search num of occurance of: "))

occurrences = myTuple.count(item)
print(f"The item {item} occurs {occurrences} times in the tuple.")

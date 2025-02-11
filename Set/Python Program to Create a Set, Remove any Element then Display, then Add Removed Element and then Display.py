mySet = {1, 12, 3, 24, 5, 6, 17, 8, 9}

rmvElement = int(input("Enter element to remove: "))

if rmvElement not in mySet:
    print("Element not found in the set.")
    exit()
if rmvElement in mySet:
    mySet.remove(rmvElement)
    print("Set after removing element: ", mySet)
    mySet.add(rmvElement)
    print("Set after adding back the removed element: ", mySet)


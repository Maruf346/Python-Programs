try:
    myList = [1, 2, 3, 4, 5]
    myDicyt = {"a": 1, "b": 2, "c": 3}
    
    index = int(input("Enter index: "))
    print(myList[index])

    myKey = input("Enter key: ")
    print(myDicyt[myKey])

except IndexError:
    print("Invalid Index.")
except KeyError:
    print("Invalid Key.")
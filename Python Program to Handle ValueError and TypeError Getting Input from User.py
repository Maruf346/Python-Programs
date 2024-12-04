try:
    myInt = int(input("Enter a number: "))
    print(myInt)

    myLen = len(myInt)
    print(myLen)

except TypeError:
    print("Invalid Type. Not a text.")
except ValueError:
    print("Invalid Value. Not an integer.")


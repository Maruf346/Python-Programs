names = []

name1 = input("Enter the name of the 1st student:")
names.append(name1)
name2 = input("Enter the name of the 2nd student:")
names.append(name2)
name3 = input("Enter the name of the 3rd student:")
names.append(name3)
name4 = input("Enter the name of the 4th student:")
names.append(name4)
name5 = input("Enter the name of the 5th student:")
names.append(name5)

for name in names:
    print(name.upper())
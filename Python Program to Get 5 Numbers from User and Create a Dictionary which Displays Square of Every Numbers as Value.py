sq_num = {}

for i in range(5):
    num = int(input(f"Enter number{i+1}: "))
    sq_num[num] = num**2 #num-->key, num^2-->value

print("square numbers are: ")
print(sq_num)
prod_dict = {}

for i in range(5):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    prod_dict[name] = price

print(prod_dict)
print("total price: "+str(sum(prod_dict.values())))
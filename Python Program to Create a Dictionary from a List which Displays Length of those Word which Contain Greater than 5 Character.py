
words = ["green", "university", "of", "Bangladesh", "GUB"]

new_dict = {i: len(i) for i in words if len(i) > 5}

print("Words with length > 5 are: ")
print(new_dict)


original_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
squared_dict = {key**2: value for key, value in original_dict.items() if isinstance(key, int)}
print(squared_dict)

my_dict = {'name': 'Maruf Hossain', 'age': 25, 'city': 'Rupganj'}
search = input("Search: ")
if search in my_dict:
    print(f"'{search}' exists in the dictionary.")
else:
    print(f"'{search}' does not exist in the dictionary.")

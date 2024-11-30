nums = {'num1': 1, 'num2': 2, 'num3': 3}

new_dict = {i: val for i, val in nums.items() if val % 2 == 0}

print(list((new_dict.keys())))
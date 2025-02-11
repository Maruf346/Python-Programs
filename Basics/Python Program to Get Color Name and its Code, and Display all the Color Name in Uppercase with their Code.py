myColors = {}

for i in range(5):
    color = input(f"Enter color name{i+1}: ")
    code = input(f"Enter color value{i+1}: ")
    myColors[color] = code

for color, code in myColors.items():
    print(f"{color.upper()} : {code}")
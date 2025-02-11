marks_dict = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    marks_dict[name] = marks

print(marks_dict)
physics = float(input("Enter marks for Physics: "))
chemistry = float(input("Enter marks for Chemistry: "))
math = float(input("Enter marks for Math: "))

tot_marks = physics + chemistry + math
avg_marks = tot_marks / 3

print(f"Hi, Your marks in Physics = {physics}, Chemistry = {chemistry}, Math = {math}.")
print(f"And Your Total Marks is {tot_marks} and Average is {avg_marks}.")

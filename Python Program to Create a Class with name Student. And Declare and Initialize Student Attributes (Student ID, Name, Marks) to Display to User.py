class Student:
    def getData(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter student name: ")
        self.marks = [float(x) for x in input("Enter marks: ").split()]       

    def showDetails(self):
        print("Student ID: ", self.id)
        print("Student Name: ", self.name)
        print("Marks: ", self.marks)
        print("Average Marks: ", sum(self.marks) / len(self.marks))
        print("Highest Marks: ", max(self.marks))
        print("Lowest Marks: ", min(self.marks))
        

obj = Student()
obj.getData()
obj.showDetails()
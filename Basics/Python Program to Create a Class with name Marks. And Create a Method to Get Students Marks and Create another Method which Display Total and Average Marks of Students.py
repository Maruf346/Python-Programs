class Marks:
    def getData(self):
        self.id = int(input("Enter student ID: "))
        self.name = input("Enter student name: ")
        self.marks = [float(x) for x in input("Enter marks: ").split()]       

    def TotMarks(self):
        return sum(self.marks)

    def AvgMarks(self):
        return self.TotMarks() / len(self.marks)

    def showDetails(self):
        print("Student ID: ", self.id)
        print("Student Name: ", self.name)
        print("Marks: ", self.marks)
        print("Average Marks: ", self.AvgMarks())
        print("Total Marks: ", self.TotMarks()) 

obj = Marks()
obj.getData()
obj.showDetails()
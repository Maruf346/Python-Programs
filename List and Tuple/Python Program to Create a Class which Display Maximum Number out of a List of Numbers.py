class MaxFinder:
    a = []
    def getData(self):
        self.a = [int(x) for x in input("Enter nums using space: ").split()]

    def showResult(self):
        print("Max number of the list is: ", max(self.a))

obj = MaxFinder()
obj.getData()
obj.showResult()
class ArithmeticOp:
    def getData(self):
        self.a = int(input("Enter num1: "))
        self.b = int(input("Enter num2: "))

    def showResult(self):
        print("Sum: ", self.a + self.b)
        print("Difference: ", self.a - self.b)
        print("Product: ", self.a * self.b)
        print("Quotient: ", self.a / self.b)
        print("Remainder: ", self.a % self.b)

obj = ArithmeticOp()
obj.getData()
obj.showResult()
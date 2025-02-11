class MyDetails:
    __myID = 221902318
    myName = "Maruf Hossain"

    def showID(self):
        print("ID: ", self.__myID)

class MyDet2(MyDetails):
    myName = "Mohibullah" #overwrites value of myName


obj = MyDetails()
print("Name: ", obj.myName)
obj.showID()
obj2 = MyDet2()
print("Name: ", obj2.myName)
obj2.showID()

# _myID = Protected: can be inherited by derived(child) classes
# __myID = private: can't be inherited by child classes
# private variables can be accessed through subclasses
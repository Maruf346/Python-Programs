class jafri:
    JafriId = 122
    _JafriName = "Faisal Zamir"

    def showID(self):
        print("ID: ", self.JafriId)
class Mock(jafri):
    _JafriName = "Mock"

obj = jafri()
print("Name: ", obj._JafriName)
obj.showID()
obj2 = Mock()
print("Name: ", obj2._JafriName)

# _JafriName = Protected: can be inherited by derived(child) classes
# __JafriName = private: can't be inherited by child classes
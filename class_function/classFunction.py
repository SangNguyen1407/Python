
class Person:
    A = 'Test school'
    B = 20
    # constructor
    def __init__(self, name: str, classNumber: str):
        self.name = name
        self.classNumber = classNumber
        
    def printInfo (self):
        print("School = ", self.A)
        print("Name   = ", self.name)
        print("Class  = ", self.classNumber)
    
    def printInfo (self, des: str):
        print("School = ", self.A)
        print("Name   = ", self.name)
        print("Class  = ", self.classNumber)
        print("Description  = ", des)
    
    

s1 = Person('NGUYEN VAN A', 'A7')
s1.printInfo('test')
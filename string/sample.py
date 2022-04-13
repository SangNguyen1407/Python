class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def myfunc(self) -> str:
        print("Hello my name: " + self.first_name)
    
    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name + " " + str(self.age) + " old."


p1 = Person ("John", "Test1",  36)
p1.myfunc()

p2 = Person ("Jack", "Test2", 25)
print(p2.first_name)

p3 = Person ("Julien", "Test3", 25)
print(p3.get_full_name())
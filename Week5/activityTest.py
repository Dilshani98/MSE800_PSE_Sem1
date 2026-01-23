class _Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.age = age
        self.address = address

    def greet(self):
        print ("greetings & facilitations from maestro "+ self.__name)


class Student(_Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print("Hi",self.__name)

Student1 = Student("Alice", "123 Main St", 20, "S12345")
Student1.greet()
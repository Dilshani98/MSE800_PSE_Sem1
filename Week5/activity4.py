#Define super class
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def personInfo(self):
        return f"Person/n ID: {self.id}/n Name: {self.name}/n"
    

#child class inherit from person
class Student(Person):
    def __init__(self, student_id, person_id, name): 
        super().__init__(person_id, name) # if we need super class attributes, we should pass them here
        self.student_id = student_id
    
    def studentInfo(self):
        return f"Student/n ID: {self.id}/n Student ID: {self.student_id}/n Name: {self.name}/n"
    
    
#child class inherit from person
class Staff(Person):
    def __init__(self, person_id, name, staffId, taxNumber):
        super().__init__(person_id, name)
        self.staffId = staffId
        self.taxNumber = taxNumber

    def staffInfo(self):
        return f"Staff/n ID {self.id}/n Staff ID: {self.staffId}/n Name: {self.name}/n Tax Number: {self.taxNumber}/n"


#child class inherit from Staff
class General(Staff):

    def __init__(self, person_id, name, staffId, taxNumber, payRate, id):
        super().__init__(person_id, name, staffId, taxNumber)
        self.payRate = payRate
        self.generalId = id

    def generalInfo(self):
        return f"General Staff/n ID {self.id}/n Staff ID: {self.staffId}/n Name: {self.name}/n Tax Number: {self.taxNumber}/n PayRate: {self.payRate}/n General ID:{self.generalId}"
    

class Academic(Staff):

    def __init__(self, person_id, name, staffId, taxNumber, publications, id):
        super().__init__(person_id, name, staffId, taxNumber)
        self.publications = publications
        self.academicId = id

    def academicInfo(self):
            return f"Academic Staff/n ID {self.id}/n Staff ID: {self.staffId}/n Name: {self.name}/n Tax Number: {self.taxNumber}/n Academic ID: {self.academicId}/n publications:{self.publications}"
    


def main():

    Student1 = Student(1, 1, "Emiliya")
    print(Student1.studentInfo)

    GeneralStaff1 = General(2,"Perera", 3, "TX12345", 30, 4)
    print(GeneralStaff1.generalInfo)

    AcademicStaff1 = Academic(3, "Hiruni", 4, "TX2566", "Violence Detection", 1) 
    print(AcademicStaff1.academicInfo)


if __name__ == "__main__":
    main()




class StudentDetails:
    def __init__(self):
        self.dic1 = {1: "Emiliya", 2: "John", 3: "Alice", 4: "Bob", 5: "Diana"}
        self.dic2 = {1: 40, 2: 30, 3: 55, 4: 80, 5: 20}

    def getPassedStudent(self):
        #merged_list = {**self.dic1, **self.dic2}
        #print(merged_list)
        filtered_list = {self.dic1[n]:v for n, v in self.dic2.items() if v >= 50}
        #filtered_list_with_names = {self.dic1[k]: v for k, v in filtered_list.items()}
        print(filtered_list)


if __name__ == "__main__":

    obj = StudentDetails()
    obj.getPassedStudent()
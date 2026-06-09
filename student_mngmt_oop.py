class Student:
    def __init__(self,id,name,mark):
        self.id=id
        self.name=name
        self.mark=mark
    def display_details(self):
        print(f"id of student: {self.id}")
        print(f"name of student: {self.name}")
        print(f"mark of student: {self.mark}")
    def calculate(self):
        if self.mark >= 90:
            print("Grade: A")
        elif self.mark >= 80:
            print("Grade: B")
        elif self.mark >= 70:
            print("Grade: C")
        elif self.mark >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
        print("---------------------")

students=[]
for i in range(3):
    id=int(input(f"Enter student {i+1} id: "))
    name=input(f"Enter student {i+1} name: ")
    mark=int(input(f"Enter student {i+1} mark: "))
    student=Student(id,name,mark)
    students.append(student)
    print("-----------------------")

for student in students:
    student.display_details()
    student.calculate()



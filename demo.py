class Name:
    def __init__(self,firstName, middleName, lastName):
        self.FirstName= firstName
        self.SecondName= middleName
        self.LastName= lastName

class Student:
    def __init__(self, sname, rollno, course):
        self.StudentName=sname
        self.RollNo=rollno
        self.Course=course


student1 =Student(101,Name("Subham","Kumar","mallick"),"Devops")
student2 =Student(102,Name("Subha","Kumara","mallik"),"Devlpoer")
student3=Student(104,Name("Subh","Kuma","mallk"),"Devs")
student4 =Student(107,Name("Suam","Ku","mallic"),"oops")


students=[student1,student2,student3,student4 ]

for student in students:
    print("StudentName : {} {}  {} \nRoll number: {}\n Course{}\n".format(student.StudentName.FirstName,student.StudentName.SecondName,student.StudentName.LastName, Student.RollNo, Student.Course))
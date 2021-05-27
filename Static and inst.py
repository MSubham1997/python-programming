class Employee:
    TotalEmployee =0


    def __init__(self,empno,ename,salary,deptno):
        self.Empno =empno
        self.Ename =ename
        self.Salary= salary
        self.Deptno=deptno
        Employee.TotalEmployee += 1

    def showEmployee(self):
        print("Employee #: {} \n Employee Name: {} \nSalary: {} \n Department :{} ".format(self.Empno,self.Ename,self.Salary,self.Deptno))


emp1= Employee(202,"Subham",15000,204)
emp2=Employee(202,"Suhas",20000,205)
print("Total employee :",Employee.TotalEmployee)
emp1.showEmployee()
emp2.showEmployee()



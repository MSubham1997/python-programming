class Employee:



    def __init__(self,empno,ename,salary,deptno):
        self.Empno =empno
        self.Ename =ename
        self.Salary= salary
        self.Deptno=deptno


    def showEmployee(self):
        print("Employee #: {} \n Employee Name: {} \nSalary: {} \n Department :{} "
              .format(self.Empno,self.Ename,self.Salary,self.Deptno))
class SalseMan(Employee):
    def __init__(self, empno, ename, salary, deptno,comm):
        self.Commision=comm
        super().__init__(empno,ename,salary,deptno)

    def showEmployee(self):
        super().showEmployee()
        print("Commision :", self.Commision)

emp=SalseMan(101,"Suhasini",20000,201,4000)
emp.showEmployee()

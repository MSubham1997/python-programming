import datetime
import calendar


class PayRollManagementSystem:


    def calculate_payroll(self,employees):
        print("Payroll Management System")
        print("============================")

        for employee in employees:
            print(f"Employee #:{Employee.Id}\nEmployee Name:{employee.name}")
            print(f"Amount :{emplyee.calulate_payroll()}")

class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class SalaryEmployee(Employee):
    def __init__(self,id,name, rate_per_day):
        super().__init__(id,name)
        self.rate_per_day=rate_per_day

    def calculate_payroll(self):
        today=datetime.datetime.now()
        totalDays= calendar.monthrange(today.year,today.month)[1]
        return self.rate_per_day*totalDays

class PartTimeEmployee(Employee):
    def __init__(self,id,name,total_hours,rate_per_hour):
        super().__init__(id,name)
        self.total_hours=total_hours
        self.rate_per_hours=rate_per_hour

    def calculate_payroll(self):
        return self.total_hours*rate_per_hour

class CommissionEmployee(SalaryEmployee):
    def __init__(self,id,name,rate_per_day,commission):
        super().__init__(id,name,rate_per_day)
        self.commission=commission

    def calculate_payroll(self):
        salary=super().calculate_payroll()
        return salary+self.commission
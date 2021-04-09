class Employee:
    def __init__(self,name,department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def check_salary(self):
        return self.salary.check_salary()

class Salary():
    def __init__(self, amount,bonus):
        self.amount = amount
        self.bonus = bonus

    def check_salary(self):
            return  f'marketer salry is {self.amount * self.bonus} with a bonus of {self.bonus}'

marketer_salary = Salary(400000,3)
marketer_employee=Employee('Joseph','Developer',marketer_salary)   
print(marketer_employee.check_salary())                     

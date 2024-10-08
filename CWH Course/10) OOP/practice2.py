class Employee:
    salary = 234
    increment = 20

    @property       #allows to return anything
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100

e = Employee()
new_salary = e.salaryAfterIncrement
print(new_salary)

e.salaryAfterIncrement = new_salary
print(e.increment)
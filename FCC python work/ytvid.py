class Employee:
    raiseamt = 1.04

    def __init__(self, first, last, pay:int) -> None:
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay
    
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseamt)
    
    def __repr__(self):
        return f'Employee(\'{self.first}\', \'{self.last}\', {self.pay})'
    
    def __str__(self):
        return f'{self.fullname()} - {self.email}'
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname() - 1)

class Developer(Employee):
    raiseamt = 1.10

    def __init__(self, first:str, last:str, pay:int, lang:str) -> None:
        super().__init__(first, last, pay)
        self.language = lang.lower().capitalize()

class Manager(Employee):
    raiseamt = 1.15

    def __init__(self, first:str, last:str, pay:int, employees = None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if isinstance(emp, Employee) and emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())
    


    

dev = Developer('Kevin', 'Thapa', 50000, 'pYTHon')
emp = Employee('Mike', 'Goldberg', 60000)
emp1 = Employee('joe', 'shmo', 43000)
man = Manager('Marston', 'Brown', 90000, [dev])


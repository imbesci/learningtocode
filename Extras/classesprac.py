


class Employee:
    num_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        '''(self, str, str, num)'''
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_employees+=1

    @property
    def fullname(self):
        '''(self) -> str'''
        return f'{self.first} {self.last}'

    @property
    def email(self):
        '''(self) -> str'''
        return f'{self.first}.{self.last}@company.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first= first
        self.last = last
        print(f'Name updated to {first} {last}')

    @fullname.deleter
    def fullname(self):
        print(f'Deleted {self.first} {self.last}!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount= amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod   #staticmethods do not take (self) as a parameter
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __str__(self):
        return f'{self.fullname()} earns {self.pay} dollars. They can be reached at {self.email}'

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

class Developer(Employee):   #class devleoper gets all the class functions/methods of Employee
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

emp_1 = Employee('John', 'Doe', 50000)
dev_1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev_2 = Developer('Test','User', 60000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


emp_1.fullname = 'Ryan Warren'

print(emp_1.fullname)

del emp_1.fullname
class Employee:
    raiseamt = 1.04

    def __init__(self, first:str, last:str) -> None:
        self.first = first
        self.last = last

    @property    
    def email(self):
        try:
            return f'{self.first.lower()}.{self.last.lower()}@email.com'
        except:
            return 'Err: enter a valid name'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None



emp = Employee('John', 'Smith')

del emp.fullname
# emp.fullname = 'Kevin Thapa'

print(emp.first)
print(emp.email)
print(emp.fullname)

emp.fullname = 'Jason Schantz'

print(emp.first)
print(emp.email)
print(emp.fullname)
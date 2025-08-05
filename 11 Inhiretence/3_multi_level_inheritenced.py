'''
here we make 3 class and one get inheriated by one'''

class Employee:
    a=1
    def p(self):
        print(self.a)

class Programmer(Employee):
    b=2
    def pp(self):
        print(self.b)

class Manager(Programmer):
    c=3
    def ppp(self):
        print(self.c)

o=Manager()
print(o.a)
print(o.b)
print(o.c)
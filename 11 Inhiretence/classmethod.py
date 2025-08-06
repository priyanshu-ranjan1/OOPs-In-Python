class Employee:
    a=12
    def show(self):
        print(f"the class value of a is {self.a}")

e=Employee()
e.a=67
e.show()
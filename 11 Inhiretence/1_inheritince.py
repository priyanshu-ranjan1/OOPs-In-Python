class Employee:
    company= "TCS"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

'''class Programmer:
    company="HCL"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

        def showLanguage(self):
            print(f"the name is {self.name} and lannguage is {self.language}")
'''
#here instead of making so much classes with functions we can inherit it 
class Programmer(Employee):
    company="InfoTech" #we replaced one company here 
    def ShowLanguage(self):
        print(f"the  name is {self.name} and he is goow with {self.Language} language" )
        #for inside progammer a programmer specific function inside progrmmaer for showing his language




a=Employee()
b=Programmer()

print(a.company,b.company)


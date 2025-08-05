#here we learned about inheriting multiple classes into one new class

class Employee:
    company= "TCS"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

class Language:
    language="python"
    def skill(self):
        print(f"{self.language}this language is know by the programmer")

class Programmer(Employee,Language): #here we can inherit multiple classes in other class too 
    company="InfoTech" #we replaced one company here 
    def ShowLanguage(self):
        print(f"the  name is {self.name} and he is goow with {self.Language} language" )
        #for inside progammer a programmer specific function inside progrmmaer for showing his language


cc=Programmer()
 #here we toook progrsammer in cc oobject and now we have all  inside cc from all classes using simple inheritence method 
cc.name = "Ranjan OP"
cc.salary = 1_00_000
cc.show()
cc.skill()
print(cc.language)
print(cc.company)
cc.ShowLanguage

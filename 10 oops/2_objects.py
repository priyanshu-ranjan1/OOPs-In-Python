#firat we should make an class o later use it as OBJECT
class Student:
    name ="Priyanshu Ranjan"
    Language = "Telugu"
    Salary = 500000 #class done

#here we made an objevt using class student
#all data o fstudent can be used as ranjan now 
#object attributes keeps high value than class value 

ranjan=Student()
print(ranjan.Salary)
print(ranjan)
print(type(ranjan))

#new class example 
class Employee:
    languages = "python"
    salary = 4000000
    location= "on-site"
    cuteness = "full"
print(Employee)

#this we declared object using the main class 
worker =  Employee()
worker.name="priyanshu ranjan"
print(worker.name)
print(worker)


ranjan=Employee()
print(ranjan.cuteness,ranjan.languages)

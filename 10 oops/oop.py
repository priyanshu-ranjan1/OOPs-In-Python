#making an class
class Student:
    name ="Priyanshu Ranjan"
    Language = "Telugu"
    Salary = 500000

ranjan=Student()
print(ranjan.Salary)
print(ranjan)
print(type(ranjan))

#here we replacend an object in the class 
Student.name="shree ranjan"
print(Student.name)

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
print(ranjan.cuteness,ranjan.languages,ranjan.location,ranjan.salary)

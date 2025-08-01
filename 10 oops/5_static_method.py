##static method if we add this with @above a fucnton it woont ask return
'''
A static method is a function inside a class that:
    Does NOT need self (so it doesn’t care about the object).
    Does NOT use cls (so it doesn’t care about the class either).
    It’s like a regular function, but kept inside a class just for organization.
'''


class Student:
    name ="Priyanshu Ranjan"
    Language = "Telugu"
    Salary = 500000 #class done

    @staticmethod
    def getInfo():
        print("kaise ho bhaiya" )  
        #if we make a function  or similar in a class then instead of giving a parameter for function we can write self which takes all data from  the class and can use it ,  and same can be used in object  like print(self.name) instaed of student.name

    
#we use static methodwhen we need a function inside the class just to organize its not much related to the class 
Student.getInfo()
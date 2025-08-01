
class Student:
    name ="Priyanshu Ranjan"
    Language = "Telugu"
    Salary = 500000 #class done

    def getInfo(self):
        print(f"the language is {self.Language}. the salary is {self.Salary}" )  
        #if we make a function  or similar in a class then instead of giving a parameter for function we can write self which takes all data from  the class and can use it ,  and same can be used in object  like print(self.name) instaed of student.name

    
hero=Student()   #made an new object 
hero.getInfo() #calling getinfo as we dont need to print it we made print inbuilt instead of a  return value 
print(hero.getInfo())   #this will print the memory location
print(Student.getInfo(hero))
        #if we make a function  or similar in a class then instead of giving a parameter for function we can write self which takes all data from  the class and can use it ,  and same can be used in object  like print(self.name) instaed of student.name
#in this none output becuase we aare [rinting a function so it is pritning none becuae it isnt returningng anything]





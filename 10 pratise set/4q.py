#Add a static method in problem 2, to greet the user with hello. 

#Write a class “Calculator” capable of finding square, cube and square root of a number.
import math

class Calculator:
    @staticmethod
    def square(n):
        return n**2
    @staticmethod
    def cube(n):
        return n**3

    @staticmethod
    def  square_root(n):
        return math.sqrt(n)
    
    @staticmethod
    def Greet():
        return ("Namaste ji , subh prabhat ")

need=input("what do u want to calculate :- \n 'square', 'cube','square root':- \n").lower()
n=int(input("enter a  number :-  "))
if need == "square":
    result = Calculator.square(n)
elif need == "cube":
    result = Calculator.cube(n)
elif need == "square_root":
    result = Calculator.square_root(n)
else:
    result = "Invalid operation selected."

print("Result:", result)
 
print(Calculator.Greet())
#Create a class with a class attribute a; create an object from it and set ‘a’ 
#directly using ‘object.a = 0’. Does this change the class attribute? 
answer="no" #i know already
class A:
    a=12

obj=A()
obj.a=0

if(A.a)==0:
    print("Yes the number has been updates to clas from the object itself")
    answer="yes"
elif(A.a)==12:
    print("no the number doesnt get updated by updtaingbthe object variable ")
    answer="no"



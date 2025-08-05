#am jsut learning inheritence here 

class Learn():
    a=18
    @staticmethod
    def add():
        print(Learn.a+1)


class Learning(Learn):
    a=19
    pass

Learn.add()#if u want to use a function direclty from a class it should be static
Learning.add() #damm we wused the inherited data from a new class

class All(Learning):
    
    def __init__(self,name):

        print("12",name,self.a)
    

All("ranjan opp")

    

#herw we learn using super 
#think we have a function here in main class , then we make a chikld class using it ,  and make alot of chnages   and suddenlyy if we need the super class original then we can call the super and it will give the original fucntion of data

class Parent:
    a=12
    b=13
    def add(self):
        print(self.a+self.b)

class child(Parent):
    a=15
    c=15
    def add(self):
        print(self.a+self.c)
        #think suddently i need data fro rom the parent class working so icll call it with super
        super().add()
        print(super().a)
        b=super().b+12
        print(b)


dd=child()
cc=Parent()

cc.add() #this is old 
dd.add() #this is new 


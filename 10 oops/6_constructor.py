class College:
    Name = "SVM"
    Location = "Bannergatta"
    Rating = 4
    Classes = 2
    Crush = "Shree"

    @staticmethod
    def love():
        print(f"i liked talking to {College.Crush} ")  # using static method to talk about my crush 

    def __init__(self, herfullname):
        self.herfullname = herfullname  # hehe i won’t reveal her full name u noob anyone reading this
        

College.love()  # calling directly like opening up my heart in public

# print(College.herfullname) 
#  this will give error because herfullname belongs to a specific object, not the class

forgetherformyfuturewife = College("ranjan")  # made a cute object just for her 
print(forgetherformyfuturewife.herfullname)  # revealing only to me what's stored in the heart 

#final summary 


class House:
    rooms = 4
    owner = "Ranjan ka chota bhai"  # default known to everyone

    def __init__(self, secret_key):
        self.secret_key = secret_key  # hidden, private for that room

room1=House("dibbi5879")
print(room1.owner)
print(room1.secret_key)

room2 = House("dibbi_5468")
room2.owner="ranjan op sister"
print(room2.secret_key)  # works perfectly, secret known only to this object


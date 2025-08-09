class Students:
    section="a"
    total_students=5

    @classmethod
    def pp(cls,name,age):
        print(f"my name is {name} and my age {age} and am from {cls.section} and in my class total students are {cls.total_students}")
        
        #if we need to work from the class itself , then we use class method 
        
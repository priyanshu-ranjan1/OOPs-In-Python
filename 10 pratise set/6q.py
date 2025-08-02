class Demo:
    def greet(slf):
        print("Hello!")

obj = Demo()
obj.greet()  # ✅ Works perfectly. slf refers to obj
################################################################3
class Demo:
    def greet(harry):
        print("Welcome!")

obj = Demo()
obj.greet()  # ✅ Still works. Python binds obj to harry

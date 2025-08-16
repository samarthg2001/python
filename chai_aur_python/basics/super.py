class A:
    def __init__(self)-> None:
        print("this is  A  class constracutor ")
        
class B(A):
    def __init__(self) -> None:
        print("this is B class contracutor")
        super().__init__()
class C(B):
    def __init__(self) -> None:
        print("This is C class constuctor ")

A()
B()
C()
obj=A()
print(id(obj))
obj2=B()
print(id(obj))
print(id(obj2))
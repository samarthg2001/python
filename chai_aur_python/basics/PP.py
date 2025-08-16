# private method and private variable

class A:
    def __init__(self) -> None:
        self.__test()
    __a=5
    __private_variable="private variable"
    def __test(self)->None:
        print("this is private method")
        

    def sample(self):
        print(self.__a, self.__private_variable)
        self.__test()

obj=A()
A()
obj.sample()

# test()

def test():
    print("hello world")

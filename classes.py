class Demo:
    def __init__(self, name, age):
        self.age = age;
        self.name = name;

    def method(abc):
        print(abc.name)
        print(abc.age)


def namespace1():
    demo1 = Demo("moe", 129)
    print(demo1.name)
    print(demo1.age)
    del demo1.age
    print(demo1.name)
    if  hasattr( demo1,"age"):
        print(demo1.age)
    else:
        print("ageless")


def namespace2():
    demo1 = Demo("larry", 27)
    demo1.method()


namespace1()
namespace2()


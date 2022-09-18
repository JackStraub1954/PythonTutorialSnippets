class SuperClass:
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def method1(self):
        print(self.prop1)
        print(self.prop2)


class SubClass(SuperClass):
    def __init__(self, prop1, prop2, prop3, prop4):
        super().__init__(prop1, prop2)
        self.prop3 = prop3
        self.prop4 = prop4

    def method1(self):
        super().method1()
        print(self.prop3)
        print(self.prop4)


def namespace1():
    sub_class = SubClass("a", "b", "c", "d")
    print(sub_class.prop1)
    sub_class.method1()


namespace1()

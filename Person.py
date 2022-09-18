class Person:
    """first class demo"""

    def __init__(self, name: object, age: int):
        self.name = name
        self.age = age

    def my_func(self) -> object:
        print("Hello my name is " + self.name + ". I am " + str(self.age) + " years old.")
        return None

    def get_name(self):
        return self.name

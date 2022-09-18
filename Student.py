from Person import Person


class Student(Person):
    """student inherits from person demo"""

    def __init__(self, name, age, grade: float):
        Person.__init__(self, name, age)
        self.grade = grade

    def __str__(self):
        result = self.name + ", age: " + str(self.age) + " grade: " + str(self.grade)
        return result

    def who_am_i(self) -> object:
        result = "I am " + self.get_name() + ". My grade is " + str(self.grade) + "."
        return result

###################################
# lambdas
###################################
import math

from Student import Student

hypot = lambda s1, s2: math.sqrt(s1 * s1 + s2 * s2)


def by_age(stu: Student):
    return stu.age


if __name__ == '__main__':
    print(hypot(3, 4))

    students = [
        Student("jane", 12, 3.9),
        Student("dick", 14, 3.1),
        Student("sally", 10, 3.5),
        Student("moe", 15, 2.5),
        Student("alice", 11, 2.9)
    ]

    # sort using key WITHOUT lambda
    students.sort(key=by_age)
    for student in students:
        print("  by age: " + str(student))
    print("     *****")

    # sort using key WITH lambda
    students.sort(key=lambda s: s.grade)
    for student in students:
        print("by grade: " + str(student))
    print("     *****")

    # sort using key WITH lambda
    students.sort(key=lambda s: s.name)
    for student in students:
        print(" by name: " + str(student))

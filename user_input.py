import sys


def namespace1():
    fname = sys._getframe().f_code.co_name
    print("=================================")
    name = input("User name: ")
    print(name)


if __name__ == '__main__':
    namespace1()


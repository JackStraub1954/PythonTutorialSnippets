import sys


def namespace1():
    fname = sys._getframe().f_code.co_name
    print("=================================")
    print(fname)
    try:
        print(x)
    except NameError:
        print("name error")
    except:
        print("misc exception")
    finally:
        print("finally")


def namespace2():
    fname = sys._getframe().f_code.co_name
    print("=================================")
    print(fname)
    x = 5
    try:
        print(x)
    except NameError:
        print("name error")
    except:
        print("misc exception")
    else:
        print("no error")
    finally:
        print("finally")


if __name__ == '__main__':
    namespace1()
    namespace2()


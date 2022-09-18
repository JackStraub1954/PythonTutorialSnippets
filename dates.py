import datetime


def namespace1():
    dt = datetime.datetime.now()
    print(dt)
    dt = datetime.datetime(2020, 5, 17, 13, 27, 59, 0)
    print(dt)
    print(dt.year)
    print(dt.strftime("%A"))


if __name__ == '__main__':
    namespace1()

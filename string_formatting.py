import sys


def namespace1():
    price = 49
    txt = "the price is {} dollars"
    print(txt.format(price))

    txt = "the price is {:.2f} dollars"
    print(txt.format(price))


if __name__ == '__main__':
    namespace1()


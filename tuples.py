def type_print(var, tab=""):
    sv_type = str(type(var))
    svar = str(var)
    print(tab + sv_type + ": " + svar)


def type_print_iterable(var):
    sv_type = str(type(var))
    print("iterable " + sv_type + ":")
    for element in var:
        type_print(element, "    ")


def namespace1():
    tuple1 = (1, 3, 5)
    (x, y, z) = tuple1
    type_print_iterable((x, y, z))

    tuple2 = ("manny", "moe", "jack" )
    tuple3 = tuple1 + tuple2
    type_print_iterable(tuple3)


def namespace2():
    tuple1 = ("manny", "moe", "jack")
    tuple2 = 2 * tuple1
    type_print_iterable(tuple2)

    tuple3 = (1, 2, 3)
    tuple4 = 2 * tuple3
    type_print_iterable(tuple4)


def namespace3():
    tuple1 = ('dick', 'jane', 'sally')
    for inx in range(len(tuple1)):
        print(tuple1[inx])


def namespace4():
    tuple1 = ("wynken", "blynken", "nod", "wynken")
    print(tuple1.index("nod"))
    print(tuple1.count("wynken"))


if __name__ == '__main__':
    namespace1()
    namespace2()
    namespace3()
    namespace4()

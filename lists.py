def namespace1(to_add: str):
    # a list of strings
    str_list_a = ["a_manny", "a_moe", "a_jack"]
    str_list_a.append("a_" + to_add)
    print(str_list_a)

    # equivalent list...
    #     ... this is a tuple:
    #                 -----------------------------
    str_list_b = list(("b_manny", "b_moe", "b_jack"))
    #            ^^^^^
    #     list ctor converts tuple to list
    str_list_b.append("b_" + to_add)
    print(str_list_b)


def namespace2(to_add: str ):
    str_tuple_a = ("manny", "moe", "jack")
    # runtime error; tuples can't be modified
    # str_tuple_a.append(to_add)
    print(str_tuple_a)

    str_list_a = list(str_tuple_a)
    str_list_a.append(to_add)
    print(str_list_a)

    # creates list of 2 ITEMS, where the first is a tuple and the second is "to_add"
    some_list_b = [str_tuple_a, to_add]
    print(len(some_list_b))
    print(some_list_b)


def namespace3(param: str):
    # all three lists equivalent to ['a', 'l', 'i', 'c', 'e']
    list_a = list(param)
    print("A: " + str(list_a))

    list_b = list("alice")
    print("B: " + str(list_b))

    list_c = list('alice')
    print("C: " + str(list_c))


def namespace4(to_add: str):
    str_list_a = ["a_manny", "a_moe", "a_jack"]
    print(str_list_a)

    # concatenate 2 lists
    str_list_a = str_list_a + list(to_add)
    print(str_list_a)


def namespace5():
    # 4 element list: string, int, tuple, float
    list_a = ["moe", 3, ('a', 'b'), 3.14]
    print("namespace5")
    print(type(list_a))
    print(len(list_a))
    print(list_a)
    print(list_a[2])

    print("range demo")
    list_b = list(range(5))
    for num in list_b:
        print(num)


def namespace6():
    list_a = [1, 2, 3, 4, 5]
    print(list_a)  # 1, 2, 3, 4, 5

    list_a.append(6)
    print(list_a)  # 1, 2, 3, 4, 5, 6

    list_a.insert(1, 1.1)
    print(list_a)  # 1, 1.1, 2, 3, 4, 5, 6

    list_a.insert(2, 1.2)
    list_a.insert(3, 1.3)
    print(list_a)  # 1, 1.1, 1.2, 1.3, 2, 3, 4, 5, 6

    # remove item with a value of 3
    list_a.remove(3)
    print(list_a)  # 1, 1.1, 1.2, 1.3, 2, 4, 5, 6

    list_a.append(200)
    list_a.append(201)
    list_a.append(202)
    print(list_a)  # 1, 1.1, 1.2, 1.3, 2, 4, 5, 201, 202, 203

    list_a.pop()
    list_a.pop()
    print(list_a)  # 1, 1.1, 1.2, 1.3, 2, 4, 5, 201

    # remove item at index 3
    list_a.pop(3)
    print(list_a)  # 1, 1.1, 1.2, 2, 4, 5, 201

    # add elements from tuple (300, 301, 302)
    list_a.extend((300, 201, 302))
    print(list_a)  # 1, 1.1, 1.2, 2, 4, 5, 201, 300, 301, 302

    # add elements from any iterable
    list_a.extend(range(20, 30, 2))
    print(list_a)  # 1, 1.1, 1.2, 2, 4, 5, 201, 300, 301, 302, 20, 22, 24, 26, 28


if __name__ == '__main__':
    namespace1("alice")
    namespace2("alice")
    namespace3("alice")
    namespace4("alice")
    namespace5()
    namespace6()



def namespace1():
    a = """line1,
    line2 222 222 222
    line3 333 333 333"""
    print(a)

    print(a[1])


def namespace2():
    text = "alice rabbit hatter queen"
    print("rabbit" in text)
    print("tweedle" in text)
    print("hare" not in text)

    if "hare" not in text:
        print("hare not in text")
    else:
        print("ooops")


def namespace3():
    text = "0123456789 abcdefghij"
    print(text[3:7])
    print(text[3:])
    print(text[-5:-2])
    print(text[-5:])
    start = -len(text)
    end = start + 3
    print( str(start) + " ... " + str(end))
    print(text[start:end])


def namespace4():
    text = "A Mouse In The House"
    print(text.upper())
    print(text)
    print(text.lower())
    print(text)
    print("===========")
    print(text.replace("o", "K"))
    print(text)
    print(text.replace("ou", "KLIJ"))
    print(text)


def namespace4():
    seq = "manny, moe, jack"

    print("splitter: ,")
    as_split = seq.split(",")
    print("type: " + str(type(as_split)))
    for token in as_split:
        print(">" + token + "<")

    print("splitter: ,<SPACE>")
    as_split = seq.split(", ")
    for token in as_split:
        print(">" + token + "<")

    print("splitter: ,<SPACE>J")
    as_split = seq.split(", j")
    for token in as_split:
        print(">" + token + "<")

    print("splitter: <DOT>")
    as_split = seq.split(".")
    for token in as_split:
        print(">" + token + "<")


def namespace5():
    money = "money"
    ice = "ice cream"
    spot = "spot"
    fmt1 = "I want {}, Sally wants {} and Jane wants {}."
    print(fmt1.format(money, ice, spot))

    fmt2 = "I want {2}, Sally wants {0} and Jane wants {1}."
    print(fmt2.format(money, ice, spot))


if __name__ == '__main__':
    namespace1()
    namespace2()
    namespace3()
    namespace4()
    namespace5()


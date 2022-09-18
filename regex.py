import re


def namespace1():
    txt = "The rain in spain"
    x = re.search("spain", txt)
    print(x)


def namespace2():
    txt = "There was rain in the plain in spain"
    x = re.findall("the", txt)
    print(x)
    x = re.findall("[Tt]her*", txt)
    print(x)


def namespace3():
    txt = "tom, dick,   harry,dick,jane, sally,       manny"
    x = re.split(",\\s*", txt)
    print(x)


def namespace4():
    txt = "tom, dick,   harry,dick,jane, sally,       manny"
    x = re.sub("manny", "moe", txt)
    print(x)

    x = re.sub("\\s+", " ", txt)
    print(x)


def namespace5():
    txt = "The rain in spain"
    x = re.search("spain", txt)
    start = x.start()
    end = x.end()
    string = txt[start:end]
    print(str(start) + "::" + str(end) + ":" + string)


def namespace6():
    txt = " The   rain   in   spain "
    x = re.sub("\\s", "9", txt)
    print(x)
    x = re.sub("\\s+", "9", txt)
    print(x)
    x = re.sub("\s+", "9", txt)
    print(x)


def namespace7():
    txt = "The rain in Spain"

    x = re.search("\\bS\\w+", txt)
    print(x.span())
    print(x.string)
    print(x.group())


if __name__ == '__main__':
    namespace1()
    namespace2()
    namespace3()
    namespace4()
    namespace5()
    namespace6()
    namespace7()

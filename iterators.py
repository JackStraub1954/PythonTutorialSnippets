class Properties:
    def __init__(self, props):
        self.props = props

    def __iter__(self):
        self.iter_inx = 0
        self.iter_max = len(self.props)
        return self

    def __next__(self):
        if self.iter_inx < self.iter_max:
            val = self.props[self.iter_inx]
            self.iter_inx += 1
            return val
        raise StopIteration


def namespace1():
    tuple_a = (100, 200, 300)
    iter_a = iter(tuple_a)
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))


def namespace2():
    tuple_a = (100, 200, 300)
    for a in tuple_a:
        print(a)


def namespace3():
    props = Properties((1, 2, 3))
    for prop in props:
        print(prop)

    props = Properties(["a", "b", "c"])
    for prop in props:
        print(prop)


namespace1()
namespace2()
namespace3()


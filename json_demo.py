import json


def namespace1():
    str_x = '{"name":"bob", "age":"30","city":"seattle"}'
    print(type(str_x))
    print(str_x)

    json_x = json.loads(str_x)
    print(json_x["age"])


def namespace2():
    py_x = {"name": "george", "city": "portland", "age": 25 }
    print(py_x)

    json_x = json.dumps(py_x)
    print(type(json_x))
    print(json_x)


def namespace3():
    print(json.dumps(30))
    print(json.dumps(30.1))
    print(json.dumps(True))
    print(json.dumps((1, 2, 3, 5)))
    print(json.dumps((1, 2, 3, 5), indent=4))
    print(json.dumps((1, 2, 3, 5), indent=4, separators=(".", " = ")))


if __name__ == '__main__':
    namespace1()
    namespace2()
    namespace3()

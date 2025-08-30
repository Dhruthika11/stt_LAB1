

def say_hi(name: str) -> str:
    return f"Hi, {name}."


def add(x: int, y: int) -> int:
    return x + y


def algebra(x: int, y: int) -> int:
    return (x * y) * (x + y) * (x ** 2)


def say_bye(name: str) -> str:
    return f"Bye, {name}."


def subtract(x: int, y: int) -> int:
    return x - y


def greater(x: int, y: int) -> bool:
    return x > y


def lesser(x: int, y: int) -> bool:
    return x < y


if __name__ == "__main__":
    print("I am writing this code for the second task of the assignment.")
    print(say_hi("Dhruthika"))
    print(add(4, 13))
    print(algebra(11, 2))
    print(add(14, 3))
    print(algebra(10, 4))
    print(add(14, -10))
    print(algebra(3, 5))
    print(add(7, 3))
    print(algebra(8, 2))
    print(greater(14, -10))
    print(greater(3, 5))
    print(greater(7, 3))
    print(greater(8, 2))
    print(lesser(14, -10))
    print(lesser(3, 5))
    print(lesser(7, 3))
    print(lesser(8, 2))
    print(say_bye("Dhruthika"))


def square(x: float | int) -> float | int:
    return x**2


def pow(x: float | int) -> float | int:
    return x**x


def outer(x: float | int, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner

# if __name__ == '__main__':
#     my_counter = outer(3, square)
#     print(my_counter())
#     print(my_counter())
#     print(my_counter())
#     print("---")
#     another_counter = outer(1.5, pow)
#     print(another_counter())
#     print(another_counter())
#     print(another_counter())

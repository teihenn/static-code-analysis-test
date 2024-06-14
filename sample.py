def greet(name):
    print("Hello, " + name + "!")


def calculate_sum(a, b):
    return a + b


if __name__ == "__main__":
    greet("World")
    result = calculate_sum(5, 3)
    print(
        "The sum is",
        result,
        "which is calculated by adding 5 and 3 together in our calculate_sum function",
    )

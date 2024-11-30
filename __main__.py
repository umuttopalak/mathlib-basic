from mathlib_basic.errors import DivideError
from mathlib_basic.operations import add, divide, multiply, subtract


def main():
    print("Addition: 1 + 2 =", add(1, 2))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 2 * 3 =", multiply(2, 3))
    try:
        print("Division: 6 / 0 =", divide(6, 0))
    except DivideError as e:
        print(e)

if __name__ == "__main__":
    main()

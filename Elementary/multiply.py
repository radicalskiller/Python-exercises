"""Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.

Input: Two arguments. Both are int
Output: Int."""


def mult_two(a, b):
    return a*b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

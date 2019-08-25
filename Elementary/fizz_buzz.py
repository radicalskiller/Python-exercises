"""You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Input: A number as an integer.
Output: The answer as a string.
Precondition: 0 < number ≤ 1000"""


def check_3(number: int) -> bool:
    return True if number % 3 == 0 else False


def check_5(number: int) -> bool:
    return True if number % 5 == 0 else False


def checkio(number: int) -> str:
    if check_3(number):
        result = 'Fizz'
        if check_5(number):
            result += ' Buzz'
    elif check_5(number):
        result = 'Buzz'
    else:
        result = str(number)
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - the first, third and second to the last for the given array.

Input: A tuple, at least 3 elements long.
Output: A tuple."""


from operator import itemgetter


"""def easy_unpack(elements: tuple) -> tuple:
    return (*[elements[0], elements[2], elements[len(elements)-2]], )"""
easy_unpack = itemgetter(0, 2, ~1)


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

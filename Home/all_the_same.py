"""In this mission you should check if all elements in the given list are equal.

Input: List.
Output: Bool.
Precondition: all elements of the input list are hashable"""


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    for i in range(1, len(elements)):
        if elements[i] != elements[i-1]:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

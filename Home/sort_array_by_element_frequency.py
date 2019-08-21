"""Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable
Precondition: elements can be ints or strings"""

def frequency_sort(items):
    counter = {}
    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    sorted_counter = sorted(counter.items(), key=lambda kv: -kv[1])

    result = []
    for kv in sorted_counter:
        for i in range(kv[1]):
            result.append(kv[0])
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

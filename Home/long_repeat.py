"""This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.
Output: Int."""

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    cnt, res = 0, 0
    if line != '':
        cnt += 1
        res += 1
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            cnt+=1
        else:
            cnt = 1
        if cnt > res:
            res = cnt
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
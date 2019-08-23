"""You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.
Precondition:
0 < pawns ≤ 8"""

d = {'a': 1,
     'b': 2,
     'c': 3,
     'd': 4,
     'e': 5,
     'f': 6,
     'g': 7,
     'h': 8}

def safe_pawns(pawns: set) -> int:
    pwns = []
    cnt = 0
    for c in pawns:
        x, y = d[c[0]], int(c[1])
        temp = [x, y]
        pwns.append(temp)
    for c in pwns:
        used = []
        for c2 in pwns:
            if c2 not in used:
                used += [c2]
                if c[1] - c2[1] == 1:
                    if c2[0] == c[0]-1 or c2[0] == c[0]+1:
                        cnt+=1
                        break
    return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns(["e7", "e6", "d5", "f5", "c4", "e4", "g4", "e8"])
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

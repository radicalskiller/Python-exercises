"""You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.

Input: A text as a string (unicode)
Output: A quantity of striped words as an integer.
Precondition:The text contains only ASCII symbols.
0 < len(text) < 105"""

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    words = re.split('\.|,| |;|-|, |\?', text)
    striped_cnt=0
    for word in words:
        print('WORD: ', word)
        word_len = len(word)
        if word_len < 2:
            continue
        cnt=1
        flg = True
        while cnt < word_len and flg:
            if word[cnt].upper() in CONSONANTS:
                if word[cnt-1].upper() not in VOWELS:
                    flg = False
                    break
            if word[cnt].upper() in VOWELS:
                if word[cnt-1].upper() not in CONSONANTS:
                    flg = False
                    break
            if (word[cnt].upper() not in CONSONANTS) and (word[cnt].upper() not in VOWELS):
                flg = False
                break
            cnt+=1
        if cnt == word_len:
            striped_cnt+=1
            print("striped")
    return striped_cnt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio('To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?') == 8

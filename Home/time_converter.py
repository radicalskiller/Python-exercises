"""You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).
Precondition:
'00:00' <= time <= '23:59'"""

def time_converter(time_24):
    time_12 = ''
    time_hh, time_mm = time_24.split(':')

    if int(time_hh) == 0:
        time_12 += '12'
    elif int(time_hh) > 12:
        time_12 += str(int(time_hh) - 12)
    else:
        time_12 += str(int(time_hh))

    time_12 += ':' + time_mm

    if int(time_hh) >= 12:
        time_12 += ' p.m.'
    else:
        time_12 += ' a.m.'
    print(time_12)
    return time_12

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

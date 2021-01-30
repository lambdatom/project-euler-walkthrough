def naive():
    words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
    }

    sum_9 = sum([len(words[i+1]) for i in range(9)])
    sum_19 = sum([len(words[i+1]) for i in range(19)])
    sum_99 = sum_19 + 8*sum_9 + 10*sum([len(words[i]) for i in range(20, 100, 10)])
    sum_999 = sum_99 + 9*sum_99 + 100*(sum_9+9*len(words[100])) + (900-9)*len('and')
    sum_1000 = sum_999 + len(words[1] + words[1000])

    return sum_1000


def solve():
    return naive()


if __name__ == "__main__":
    print(solve())

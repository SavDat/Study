def split_decode_series(string):
    n = ''
    for i in string:
        if i.isdigit():
            n += i
            continue
        yield (int(n or 1), i)  # (11 a) ...
        n = ''


def decode_series(string):
    s = ''
    for i in list(string):  # [(11, 'a'), (3, 'b'), (1, 'B')]
        s += i[0] * i[1]
    return s


def rle_decode(string):
    return decode_series(split_decode_series(string))


print(rle_decode('11a3bB'))  # aabbbB

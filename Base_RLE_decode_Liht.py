a = ''
for i in input():
    if i.isdigit():
        a += i
        continue
    print(i * int(a or 1), end = '')
    a = ''

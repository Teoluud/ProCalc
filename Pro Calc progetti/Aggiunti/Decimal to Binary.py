def binary():
    dec = int(input('Enter a number--> '))
    lst = []
    while dec / 2 != 0:
        n = dec % 2
        lst.append(n)
        dec = int(dec / 2)
    lst.sort(reverse=True)
    print(''.join(str(x) for x in lst))

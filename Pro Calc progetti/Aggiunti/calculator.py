def calc(x, op, y):
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        print(x / y)


clc = input('Write the calculation--> ')
lst = list(clc)

a = int(lst[0])
b = int(lst[2])
s = lst[1]

calc(a, s, b)

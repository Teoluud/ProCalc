import math

while True:
    n = input('Inserire numeratore  --> ')
    if n == 'esc' or n == 'ESC':
        print('''
Il programma verrà chiuso...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
        break

    else:
        d = input('Inserire denominatore--> ')
        n = int(n)
        d = int(d)
        if d < 0:  # se il denom è <0
            n *= -1  # porto il meno al numeratore
            d *= -1
        MCD = math.gcd(n, d)  # calcolo l'MCD
        n /= MCD  # semplifico
        d /= MCD
        print('   ' + str(n))
        print('  ------')
        print('   ' + str(d))

        loop = input('Continuare? S/N ')
        if loop == 's' or loop == 'S':
            print('''
Torno all'inizio...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
            continue
        elif loop == 'n' or loop == 'N':
            print('''
Il programma verrà chiuso...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
            break
        else:
            print('''
Scegliere una delle opzioni, grazie!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
            continue

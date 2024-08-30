from math import gcd

print('''made by Matteo Gros Jacques
con un lievissimo aiutino di Luca Dalla Villa xd lol lol :)
''')
while True:
    i1 = int(input('Inserisci il primo indice di radice -> '))  # indice prima radice
    r1 = input('Inserisci il primo radicale -> ')  # radicando prima radice
    i2 = int(input('Inserisci il secondo indice di radice -> '))  # indice seconda //
    r2 = input('Inserisci il secondo radicale -> ')  # radicando seconda //
    mcm = (i1 * i2) / gcd(i1, i2)  # calcolo mcm
    e1 = mcm / i1  # esponente primo radicando
    e2 = mcm / i2  # esponente secondo radicando
    i1 = mcm  # l'indice diventa pari all'mcm
    i2 = mcm  # l'indice diventa pari all'mcm
    print('\n' + str(i1) + '√[(' + str(r1) + ')^' + str(e1) + ']')
    print(str(i2) + '√[(' + str(r2) + ')^' + str(e2) + ']')

    loop = input('Continuare? S/N ')
    if loop == 's' or loop == 'S':
        print('''
Torno all'inizio...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
        continue
    else:
        print('''
Chiudo il programma...
''')
        break

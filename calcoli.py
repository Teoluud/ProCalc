import math


def calc():
    print('\nHai scelto Calcolo Base!')
    try:
        clc = input('Inserire il calcolo -> ')
        if clc.count('+') == 1:
            dig = clc.split('+')
            a = float(dig[0])
            b = float(dig[-1])
            print('Il risultato è... ' + str(a + b))
        elif clc.count('-') == 1:
            dig = clc.split('-')
            a = float(dig[0])
            b = float(dig[-1])
            print('Il risultato è... ' + str(a - b))

        elif clc.count('*') == 1:
            dig = clc.split('*')
            a = float(dig[0])
            b = float(dig[-1])
            print('Il risultato è... ' + str(a * b))

        elif clc.count('/') == 1:
            dig = clc.split('/')
            a = float(dig[0])
            b = float(dig[-1])
            print('Il risultato è... ' + str(a / b))

        else:
            print('I calcoli disponibili sono: + - * /')

    except ValueError:
        print('\nInserire un calcolo, grazie!')
    except Exception as i:
        print(i)


def radians():
    print('\nHai scelto Radianti-Gradi!')
    try:
        rad = float(input('Inserire angolo -> '))
        deg = (180 / math.pi) * rad
        print('\nIl risultato è... ' + str(deg))
    except ValueError:
        print('\nInserire un numero, grazie!')
    except Exception as i:
        print(i)


def binary():
    print('\nHai scelto Decimale-Binario!')
    try:
        dec = int(input('Inserisci il numero -> '))
        lst = []
        while dec / 2 != 0:
            n = dec % 2
            lst.append(n)
            dec = int(dec / 2)
        lst.sort(reverse=True)
        bnr = (''.join(str(x) for x in lst))
        print('\nIl risultato è... ' + str(bnr))
    except ValueError:
        print('\nInserire un numero, grazie!')
    except Exception as i:
        print(i)


def esponente():
    print('\nHai scelto Esponenziale!')
    try:
        a = float(input('Inserisci la base -> '))
        b = float(input('Inserisci l\'esponente -> '))
        print('\nIl risultato è... ' + str(a ** b))
    except ValueError:
        print('\nInserire solo cifre, grazie!')
    except Exception as i:
        print(i)


def radice():
    print('\nHai scelto Radice!')
    try:
        i = int(input('Inserisci l\'indice --> '))
        r = int(input('Inserisci il radicando -> '))
        ris = pow(r, 1 / i)
        print('\nIl risultato è: ' + str(ris))
    except ValueError:
        print('\nScegli un radicando positivo o nullo!')
    except Exception as i:
        print(i)


def fattoriale():
    print('\nHai scelto Fattoriale!')
    try:
        a = int(input('Inserisci il numero -> '))
        print('\nIl risultato è... ' + str(math.factorial(a)))
    except ValueError:
        print('\nScegli un numero intero e positivo!')
    except Exception as i:
        print(i)


def percentuale():
    print('\nHai scelto Percentuale!')
    try:
        a = float(input('Inserisci la percentuale -> '))
        tot = float(input('Inserisci il totale -> '))
        print('\nIl ' + str(a) + '% di ' + str(tot) + ' è... ' + str(a / 100 * tot))
    except ValueError:
        print('\nInserire solo cifre!')
    except Exception as i:
        print(i)


def frazioni():
    print('\nHai scelto Semplificazione di Frazioni!')
    n = int(input('Inserisci numeratore -> '))
    d = int(input('Inserisci denominatore -> '))
    try:
        if n % d == 0:
            print(str(n / d))
        else:
            if d < 0:
                n *= -1
                d *= -1
            mcd = math.gcd(n, d)
            n /= mcd
            d /= mcd
            print('   ' + str(n))
            print('  ------')
            print('   ' + str(d))
    except Exception as i:
        print(i)


def equazioni():
    print('\nHai scelto Equazione di Secondo Grado!')
    try:
        a = float(input('Inserisci coefficiente di secondo grado -> '))
        b = float(input('Inserisci coefficiente di primo grado ---> '))
        c = float(input('Inserisci termine noto ------------------> '))
        if a == 0:
            print("L'equazione è di primo grado!")
        else:
            if b == 0 and c != 0:  # equazione pura
                print(str(a) + 'x^2+' + str(c) + '=0')
                if c > 0:
                    print('\nEquazione impossibile')
                else:
                    x1 = -(math.sqrt(-c / a))
                    x2 = +(math.sqrt(-c / a))
                    n = int(-c)
                    d = int(a)
                    if n % d == 0:
                        if math.sqrt(-c / a) != int(math.sqrt(-c / a)):
                            print('\nx1=-√' + str(-c / a))
                            print('x2=√' + str(-c / a))
                        else:
                            print('\nx1=' + str(x1))
                            print('x2=+' + str(x2))
                    else:
                        if d < 0:
                            n *= -1
                            d *= -1
                        mcd = math.gcd(n, d)
                        n /= mcd
                        d /= mcd
                        if math.sqrt(n) != int(math.sqrt(n)):
                            xn = '√' + str(n)
                        else:
                            xn = str(int(math.sqrt(n)))

                        if math.sqrt(d) != int(math.sqrt(d)):
                            xd = '√' + str(d)
                        else:
                            xd = str(int(math.sqrt(d)))

                        print('     ' + str(xn))
                        print('x1=- -----')
                        print('     ' + str(xd))
                        print('     ' + str(xn))
                        print('x2=  -----')
                        print('     ' + str(xd))

            elif b != 0 and c == 0:  # equazione spuria
                print(str(a) + 'x^2+' + str(b) + 'x=0')
                x1 = 0
                x2 = -(b / a)
                print('\nx1=' + str(x1))
                n2 = int(-b)
                d2 = int(a)
                if n2 % d2 == 0:
                    print('x2=' + str(x2))
                else:
                    if d2 < 0:
                        n2 *= -1
                        d2 *= -1
                    mcd2 = math.gcd(n2, d2)
                    n2 /= mcd2
                    d2 /= mcd2
                    print("    " + str(n2))
                    print('x2= -----')
                    print('    ' + str(d2))
            elif b != 0 and c != 0:
                print(str(a) + 'x^2+' + str(b) + 'x+' + str(c) + '=0')

                if b % 2 == 0:  # formula ridotta
                    delta4 = (b / 2) ** 2 - a * c
                    print('delta/4=' + str(delta4))

                    if delta4 < 0:  # impossibile
                        print('\nNon ci sono soluzioni in campo reale')
                    else:
                        x1 = (-b / 2 - (math.sqrt(delta4))) / a
                        x2 = (-b / 2 + (math.sqrt(delta4))) / a

                        if math.sqrt(delta4) != int(math.sqrt(delta4)):
                            print('\nx1= (-' + str(b / 2) + '-√' + str(delta4) + ')/' + str(a))
                            print('x2= (-' + str(b / 2) + '+√' + str(delta4) + ')/' + str(a))
                        else:
                            n1 = int(-b / 2 - (math.sqrt(delta4)))
                            n2 = int(-b / 2 + (math.sqrt(delta4)))
                            d1 = int(a)
                            d2 = int(a)
                            if n1 % d1 == 0:
                                print('x1=' + str(x1))
                            else:
                                if d1 < 0:
                                    n1 *= -1
                                    d1 *= -1
                                mcd1 = math.gcd(n1, d1)
                                n1 /= mcd1
                                d1 /= mcd1
                                print('     ' + str(n1))
                                print('x1= ------')
                                print('     ' + str(d1))

                            if n2 % d2 == 0:
                                print('x2=' + str(x2))
                            else:
                                if d2 < 0:
                                    n2 *= -1
                                    d2 *= -1
                                mcd2 = math.gcd(n2, d2)
                                n2 /= mcd2
                                d2 /= mcd2
                                print('     ' + str(n2))
                                print('x2= ------')
                                print('     ' + str(d2))

                else:  # formula intera
                    delta = b * b - 4 * a * c
                    print('delta=' + str(delta))

                    if delta < 0:  # impossibile
                        print('\nNon ci sono soluzioni in campo reale')
                    else:
                        x1 = (-b - (math.sqrt(delta))) / (2 * a)
                        x2 = (-b + (math.sqrt(delta))) / (2 * a)

                        if math.sqrt(delta) != int(math.sqrt(delta)):
                            print('\nx1= (-' + str(b) + '-√' + str(delta) + ')/' + str(2 * a))
                            print('x2= (-' + str(b) + '+√' + str(delta) + ')/' + str(2 * a))
                        else:
                            n1 = int(-b - (math.sqrt(delta)))
                            n2 = int(-b + (math.sqrt(delta)))
                            d1 = int(2 * a)
                            d2 = int(2 * a)
                            if n1 % d1 == 0:
                                print('x1=' + str(x1))
                            else:
                                if d1 < 0:
                                    n1 *= -1
                                    d1 *= -1
                                mcd1 = math.gcd(n1, d1)
                                n1 /= mcd1
                                d1 /= mcd1
                                print('     ' + str(n1))
                                print('x1= ------')
                                print('     ' + str(d1))

                            if n2 % d2 == 0:
                                print('x2=' + str(x2))
                            else:
                                if d2 < 0:
                                    n2 *= -1
                                    d2 *= -1
                                mcd2 = math.gcd(n2, d2)
                                n2 /= mcd2
                                d2 /= mcd2
                                print('     ' + str(n2))
                                print('x2= ------')
                                print('     ' + str(d2))
    except Exception as i:
        print(i)


def primi():
    print('\nHai scelto Verifica di Numero Primo!')
    while True:
        try:
            n = int(input('Inserire il numero -> '))
            if n < 0:
                print('Segliere un numero maggiore o uguale a 1!')
                continue
            else:
                div = 2
                count = 0
                while div < n / 2 and count == 0:  # il divisore è massimo metà del numero, per risparmiare tempo
                    if n % div == 0:  # divisibile per il divisore
                        count += 1  # aumenta il conto di uno
                    div += 1
                if count == 0:
                    print('\nNumero primo!')
                    break
                else:
                    print('\nNumero non primo!')
                    break
        except ValueError:
            print('\nInserire solo numeri interi, grazie!')
        except Exception as i:
            print(i)


def fibonacci():
    print('\nHai scelto Sequenza di Fibonacci!')
    try:
        n = int(input('Inserisci numero massimo numeri -> '))
        a, b = 1, 1
        for i in range(n):
            print(a, end=' ')
            a, b = b, a + b
            print()
    except ValueError:
        print('Inserire numero intero positivo!')
    except Exception as i:
        print(i)

import math

while True:
    try:
        a = float(input('Inserisci coefficiente di secondo grado -> '))
        b = float(input('Inserisci coefficiente di primo grado   -> '))
        c = float(input('Inserisci termine noto                  -> '))
        if a == 'esc' or b == 'esc' or c == 'esc':
            break
        elif a == 0:
            print("L'equazione è di primo grado!")
        else:
            if b == 0 and c != 0:  # equazione pura
                if c > 0:
                    print('Non ci sono soluzioni in campo reale')
                else:
                    print(str(a) + 'x^2+' + str(c) + '=0')
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
                        MCD = math.gcd(n, d)
                        n /= MCD
                        d /= MCD
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
                    MCD2 = math.gcd(n2, d2)
                    n2 /= MCD2
                    d2 /= MCD2
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
                                MCD1 = math.gcd(n1, d1)
                                n1 /= MCD1
                                d1 /= MCD1
                                print('     ' + str(n1))
                                print('x1= ------')
                                print('     ' + str(d1))

                            if n2 % d2 == 0:
                                print('x2=' + str(x2))
                            else:
                                if d2 < 0:
                                    n2 *= -1
                                    d2 *= -1
                                MCD2 = math.gcd(n2, d2)
                                n2 /= MCD2
                                d2 /= MCD2
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
                                MCD1 = math.gcd(n1, d1)
                                n1 /= MCD1
                                d1 /= MCD1
                                print('     ' + str(n1))
                                print('x1= ------')
                                print('     ' + str(d1))

                            if n2 % d2 == 0:
                                print('x2=' + str(x2))
                            else:
                                if d2 < 0:
                                    n2 *= -1
                                    d2 *= -1
                                MCD2 = math.gcd(n2, d2)
                                n2 /= MCD2
                                d2 /= MCD2
                                print('     ' + str(n2))
                                print('x2= ------')
                                print('     ' + str(d2))

        loop = input('\nContinuare? S/N ')
        if loop == 'S' or loop == 's':
            print('''
Torno all'inizio...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
            continue
        elif loop == 'N' or loop == 'n':
            print('''
Chiudo il programma...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
            break
        else:
            print('''
Scegliere una delle opzioni, grazie!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
            continue

    except Exception as i:
        print(i)

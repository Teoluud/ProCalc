while True:
    i = int(input("\nInserire l'indice di radice -> "))
    r = int(input("Inserire il radicando --------> "))
    ris = pow(r, 1/i)
    print('\nIl risultato della radice è: ' + str(ris))
    loop = input('Continuare? s/n ')
    if loop == 's' or loop == 'S':
        continue
    else:
        break

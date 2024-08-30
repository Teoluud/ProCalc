while True:
    try:
        n = int(input('Inserire numero -> '))
        if n<1:
            print('\nInserire numero maggiore o ugale a 1!\n')
            continue
        else:
            div = 2
            count = 0
            while div<n/2 and count == 0:
                if n%div == 0:
                    count += 1
                div += 1
            if count == 0:
                print('\nNumero primo!')
            else:
                print('\nNumero non primo!')
    except ValueError:
        print('\nInserire solo numeri interi, grazie!\n')
        continue

    loop = input('Continuare? S/N ')
    if loop == 'S' or loop == 's':
        print('')
        continue
    else:
        break
import calcoli
import time

t = 3  # delay prima della chiusura

print('''
    Benvenuto in ProCalc!
    Creato da: Matteo''')
while True:
    print('''
    Ecco l\'elenco delle opzioni disponibili:
    -Calcolo Base: scegliere 1;
    -Esponenziale: scegliere 2;
    -Radice: scegliere 3;
    -Percentuale: scegliere 4;
    -Fattoriale: scegliere 5;
    -Semplificazione di Frazione: scegliere 6;
    -Equazione di Secondo Grado: scegliere 7;
    -Verifica di Numero Primo: scegliere 8;
    -Radianti-Gradi: scegliere 9;
    -Decimale-Binario: scegliere 10;
    -Sequenza di Fibonacci: scegliere 11;
    -Per uscire dal programma, digitare ESC.''')

    scelta = input("Inserisci il numero corrispondente all'azione desiderata ---> ").lower()

    match scelta:
        case '1':
            calcoli.calc()
        case '2':
            calcoli.esponente()
        case '3':
            calcoli.radice()
        case '4':
            calcoli.percentuale()
        case '5':
            calcoli.fattoriale()
        case '6':
            calcoli.radice()
        case '7':
            calcoli.equazioni()
        case '8':
            calcoli.primi()
        case '9':
            calcoli.radians()
        case '10':
            calcoli.binary()
        case '11':
            calcoli.fibonacci()
        case 'esc':
            print('\nIl programma verrà ora chiuso!')
            time.sleep(t)
            break
        case _:
            print('''
SCEGLIERE UNA DELLE OPZIONI DISPONIBILI, GRAZIE!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
            continue

    loop = input('\nDesideri continuare ad utilizzare il programma? S/N ')
    if loop == 's' or loop == 'S':
        print('''
Torno al menu principale...
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue
    elif loop == 'n' or loop == 'N':
        print('''
Grazie di aver utilizzato ProCalc!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        time.sleep(t)
        break
    else:
        print('''
SCEGLIERE UNA DELLE DUE OPZIONI, GRAZIE!
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue

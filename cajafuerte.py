from random import randrange

intentos = 7
vidas = 2
bomba_1 = randrange(0, 9)
bomba_2 = randrange(0, 9)
casillas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if bomba_1 == bomba_2:
    bomba_2 = randrange(0, 9)

array = []

for i in range(9):
    array.append(0)

array[bomba_1] = 'bomba'
array[bomba_2] = 'bomba'

# print(array)
print('-' * 60)
print(casillas)

for element in array:
    print('-' * 60)
    x = int(input('Selecciona la casilla: ')) - 1

    while x > 8 or x < 0:
        print('Casilla no valida')
        x = int(input('Selecciona la casilla: ')) - 1

    while casillas[x] == 'X':
        print('Casilla ya seleccionada, pida otra')
        x = int(input('Selecciona la casilla: ')) - 1

    casillas[x] = 'X'
    intentos = intentos - 1
    if array[x] == 'bomba':
        array[x] = 1
        vidas = vidas - 1
        intentos = intentos + 1
        print('Te salio una bomba')
    if array[x] == 0:
        array[x] = 1
    if vidas == 0:
        print('Perdiste')
        break
    if intentos == 0:
        print('Ganaste!!!!')
        break

    print('-' * 60)
    print('Cantidad de vidas: ', vidas)
    print(casillas)
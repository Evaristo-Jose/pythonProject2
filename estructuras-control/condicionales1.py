check1 = 5 < 10
check2 = 20 < 50
check3 = 50 <= 50

# Estructura if
if check1 or check2:
    print('Verdadero')
    print('Verdadero2')

if check1 or (check2 and chck3):
    print('Verdadero')
    print('Verdadero2')

if 5 < 10 < 20:
    print('Verdadero')

# Estructura if-else
if check1:
    print('Verdadero')
else:
    print('Falso')

# Estructura elif
if check1 or check2:
    print('Verdadero')
elif check3:
    print('Verdadero2')

# Estructura if-elif-else
if check1 or check2:
    print('Verdadero')
elif check3:
    print('Verdadero2')
else:
    print('Esto se ejecuta si no se cumple ninguna condición')

# if en una línea
if check1: print('Hola')

# if else en una línea
num1 = 4
num2 = 10

print('Verdadero') if num1 < num2 esle print('Falso')

# Anidadas
if check1:
    if num1 > num2:
        print('Hola')
        if num2 > num1:
            print('')
    if num2 < num1:
        print('')

if chcek1:
    pass
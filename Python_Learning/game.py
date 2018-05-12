u"""Adivina el número."""
import random

print('-------------------------------------------')
print('            ADIVINA EL NUMERO')
print('-------------------------------------------')
print()

numero = random.randint(0, 100)
nombre = input('¿Como te llamas? ')
adivina = -1


while adivina != numero:
    adivina = input('Adivina que numero estoy pensando de 0 a 100? ')
    adivina = int(adivina)
    if adivina > numero:
        print('{}, el número {} es demasiado alto'.format(nombre, adivina))
    elif adivina < numero:
        print('{}, el número {} es demasiado bajo'.format(nombre, adivina))
    else:
        print('¡Enhorabuena {}, {} es el numero!'.format(nombre, adivina))

print('')

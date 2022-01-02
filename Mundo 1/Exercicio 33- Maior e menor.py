numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
maior = numero1
menor = numero1

if numero2 > maior and numero2 > numero3:
    maior = numero2
elif numero3 > maior and numero3 > numero2:
    maior = numero3


if numero2 < menor and numero2 < numero3:
    menor = numero2
elif numero3 < menor and numero3 < numero2:
    menor = numero3

print('O maior número é {} e o menor é {} '.format(maior, menor))

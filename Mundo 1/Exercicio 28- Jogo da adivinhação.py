import random

numero = random.randint(0, 5)
adivinha= int(input('Adivinhe um número de 0 a 5:'))

print('O número é: {}'.format(numero))

if numero == adivinha : 
  print('Você acertou')
else:
  print('Você errou, tente novamente')
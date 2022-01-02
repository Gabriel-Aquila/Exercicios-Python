maior = 0
menor = 900
for c in range(0, 5):
    peso = int(input('Qual é o sue peso?  '))
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso

print('O maior peso é {}Kg e o menor é {}Kg'.format(maior, menor))

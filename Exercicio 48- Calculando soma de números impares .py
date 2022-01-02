soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma de todos os valores é {}'.format(soma))

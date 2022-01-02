numero = int(input('Digite um número \n'))
tot = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[34m{}\033[m'.format(c), end=' ')
        tot += 1
    else:
        print('\033[m{}'.format(c), end=' ')
if tot == 2:
    print('\nO número é primo!')
else:
    print('\nO número não é primo!')

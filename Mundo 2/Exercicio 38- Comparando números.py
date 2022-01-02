numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
maior = numero1


if numero1 == numero2:
    print('\033[1;33;33m Os números são iguais, não há maior \033[m')
elif numero1 < numero2:
    maior = numero2
    print('O número {}{}{} é o maior'.format(
        '\033[1;36;36m', numero2, '\033[m'))
else:
    print('O número {}{}{} é maior '.format(
        '\033[1;36;36m', numero1, '\033[m'))

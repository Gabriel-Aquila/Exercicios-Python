valorDaCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? R$: '))
anosPagamento = float(input('Em quantos anos você vai pagar? '))

prestação = valorDaCasa/(anosPagamento*12)

print('{}A prestação é R$:{:.2f}{}'.format('\033[1;33;33m',prestação,'\033[m'))

if prestação > salario*0.30 :
  print('{} O empréstimo foi negado, você não pode pagar{}'.format('\033[1;31;31m','\033[m'))
else: 
  print('{}O empréstimo foi aceito!!! {}'.format('\033[1;32;32m','\033[m'))

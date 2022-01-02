salario= float(input('Digite seu sálario: '))

if salario <= 1250 :
 salario= salario+(salario*0.15)
else:
  salario= salario+(salario*0.10)

print('Seu novo salário é R$:{} '.format(salario))
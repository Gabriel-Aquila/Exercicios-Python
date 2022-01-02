velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80 :
  multa= 7.00*(velocidade-80)
  print('Sua multa é de R$:{:.2f}'.format(multa))

else:
  print('Você esta no limite!')
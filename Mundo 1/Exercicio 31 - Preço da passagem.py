distancia = float(input('Qual é a distancia da sua viagem? '))

if distancia <= 200 :
  passagem = distancia *0.50 
else:
  passagem = distancia*0.45

print('O preço da passagem é R$:{:.2f}'.format(passagem))
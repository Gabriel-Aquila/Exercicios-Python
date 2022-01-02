tempo = float(input('Quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km foram rodados? '))
total = (60*tempo)+(0.15*Km)
print('O preço do aluguel é R$:{:.2f}'.format(total))
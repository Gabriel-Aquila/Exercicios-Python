preço = float(input('Qual é o preço do produto? R$:'))
pagamento = int(input(
    'Qual é a forma de pagamento?\n 1.Dinheiro \n 2.A vista no cartão \n 3.Duas vezes no cartão \n 4.Quatro vezes no cartão\n'))
pagar = 0

if pagamento == 1:
    pagar = preço-(preço*0.10)


elif pagamento == 2:
    pagar = preço-(preço*0.5)

elif pagamento == 3:
    pagar = preço

elif pagamento == 4:
    pagar = preço+(preço*0.20)

print('O produto custa R$:{} e você deve pagar R$:{}'.format(preço, pagar))

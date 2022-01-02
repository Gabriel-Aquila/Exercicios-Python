media = 0
total = 0
menor = 0
maisVelho = ''
idadeMaisVelho =int(0)
for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Qual é a sua idade, {}? '.format(nome)))
    sexo = input('Você é homem ou mulher?  ').strip().upper()
    total += int(idade)
    if idadeMaisVelho < int(idade) and sexo == 'HOMEM':
        idadeMaisVelho = idade
        maisVelho = nome
    if sexo == 'MULHER' and int(idade) < 20:
        menor = menor + 1
media = total/4
print('A média de idade do grupo é {}'.format(media))
print('O homem mais velho é o {} e tem {} anos'.format(maisVelho,idadeMaisVelho))

if menor>1:
  print('{} mulheres tem menos de 20 anos'.format(menor))
else:
   print('{} mulher tem menos de 20 anos'.format(menor))

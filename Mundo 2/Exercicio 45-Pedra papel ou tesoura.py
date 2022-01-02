import random

jogador = input('\nEscolha: \n 1.Pedra \n 2.Papel \n 3.Tesoura \n\n Jogador: ')

sorteio = ['pedra', 'papel', 'tesoura']
computador = random.choice(sorteio)

print(' Computador:', computador)

if computador == jogador:
    print('Deu empate')
elif jogador == 'tesoura' and computador == 'pedra':
    print('O computador venceu')

elif jogador == 'pedra' and computador == 'papel':
    print('O computador venceu')

elif jogador == 'papel' and computador == 'tesoura':
    print('O computador venceu')


if computador == 'tesoura' and jogador == 'pedra':
    print('O jogador venceu')

elif computador == 'pedra' and jogador == 'papel':
    print('O jogador venceu')

elif computador == 'papel' and jogador == 'tesoura':
    print('O jogador venceu')

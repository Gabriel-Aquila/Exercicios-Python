import random
aluno1=input('Digite o nome do aluno: ')
aluno2= input('Digite o nome do aluno: ')
aluno3= input('Digite o nome do aluno: ')
aluno4= input('Digite o nome do aluno: ')
sorteado= [aluno1,aluno2,aluno3,aluno4]
sorteio= random.choice(sorteado)
print('O aluno sorteado é {}'.format(sorteio))
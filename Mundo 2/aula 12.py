nome = str(input('Qual é o seu nome? '))

if nome == 'Aquila':
    print('Que nome bonito')
elif nome == 'João' or nome == 'Pedro':
    print('Seu nome é bem comum no Brasil')
else:
    print('Seu nome é tão normal...')

print('Tenha um bom dia, {}{}{}[m'.format('\033[1;36;40m',nome,'\033'))

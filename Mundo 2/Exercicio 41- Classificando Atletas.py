idade = int(input('Qual é a sua idade? '))
nome = input('Qual é o seu nome? ').strip()

if idade <= 9 :
  print('A sua categoria é \033[0;33;40m MIRIM \033[m,\033[0;36;40m{}\033[m'.format(nome))
elif idade <= 14:
  print('A sua categoria é \033[0;33;40m INFANTIL \033[m,\033[0;36;40m{}\033[m'.format(nome))
elif idade <= 19:
  print('A sua categoria é \033[0;33;40m JUNIOR \033[m,\033[0;36;40m{}\033[m'.format(nome))
elif idade <= 20 :
  print('A sua categoria é \033[0;33;40m SÊNIOR \033[m,\033[0;36;40m{}\033[m'.format(nome))
elif idade> 20 :
  print('A sua categoria é \033[0;33;40m MASTER \033[m,\033[0;36;40m{}\033[m'.format(nome))
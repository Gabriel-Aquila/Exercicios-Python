import datetime
ano=0
data = datetime.date.today().year
idade = int(data) - ano
maior=0
menor=0
for c in range(0,7):
  ano = int(input('Em que ano você nasceu?\n'))
  data = datetime.date.today().year
  idade = int(data) - ano
  if idade >= 18:
      print('\033[32m Você é maior de idade\033[m')
      maior+=1
  else:
      print('\033[0;33;40mVocê é menor de idade!\033[m')
      menor+=1
print('{} pessoas são maior de idade e {} pessoas são menores de idade'.format(maior,menor))

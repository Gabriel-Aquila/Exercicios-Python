from datetime import date

atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual-ano

if idade < 18:
    print('\033[0;33;40m Você ainda ira se alistar no serviço militar \033[m')
    data = 18-idade
    print('faltam {} anos para você se alistar'.format(data))
elif idade == 18:
    print('\033[0;32;40m Você deve se alistar no serviço militar!!!\033[m')
else:
    print('\033[0;31;40m Já passou do seu tempo de alistamento \033[m')
    data = idade - 18
    print('Se passaram {} anos desde a data do seu alistamento'.format(data))

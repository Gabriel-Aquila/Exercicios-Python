nota1= float(input('Qual sua primeira nota? '))
nota2= float(input('Qual sua segunda nota? '))
media= (nota1+nota2)//2

if media < 5.0 :
  print('\033[0;31;40m Você foi reprovado! Sua média é {}\033[m'.format(media))
elif media >= 5.0 and media <= 6.9 :
  print('\033[0;33;40m Você esta de recuperação! Sua média é {} \033[m'.format(media))
elif media > 7.0: 
  print('\033[0;32;40m Parabéns, você foi aprovado. Sua média é {} \033[m'.format(media)
  )

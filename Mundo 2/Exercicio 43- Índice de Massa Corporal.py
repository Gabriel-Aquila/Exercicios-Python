peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura**2) 

if imc <18.5 :
  print('Você está abaixo do peso')
elif imc >= 18.5 and imc<25 :
  print('Você esta no peso ideal')
elif imc >= 25 and imc <=30 :
  print('Você esta com sobrepeso')
elif imc >= 30 and imc < 40:
  print('Você esta obeso ')
elif imc >40 :
  print ('Você esta com obesidade mórbida,procure um médico')

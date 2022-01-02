numero = int(input('Digite um número inteiro qualquer: '))
escolha= int(input('Escolha a base de conversão \n 1. Binario \n 2. Octal \n 3. Hexadecimal '))

if escolha == 1 :
  print('O número {} equivale a {} em binario '.format(numero,bin(numero) [2:]))

elif escolha == 2 :
  print('O número {} equivale a {} em Octal '.format(numero,oct(numero) [2:]))

elif escolha == 3 :
  print('O número {} equivale a {} em Hexadecimal'.format(numero,hex(numero)[2:]))

else:
    print('\033[33;43;40m Opção invalida \033[m')
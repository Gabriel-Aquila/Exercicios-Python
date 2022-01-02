lado1=float(input('Digite o tamanho do primeiro lado: '))
lado2= float(input('Digite o tamanho do segundo lado:'))
lado3=float(input('Digite o tamanho do terceiro lado: '))

if lado1<lado2+lado3 and lado2<lado3+lado1 and lado3<lado1+lado2 :
  print('O triangulo pode existir')

else:
  print('Não é possivel haver um triangulo')
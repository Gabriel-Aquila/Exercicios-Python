largura= float(input('Digite a largura da parede '))
altura = float(input('Digite a altura da parede '))

area= altura*largura

tinta= area/2

print('São necessarios {} litros de tinta para pintar {} metros quadrados da parede'.format(tinta,area))
import math
oposto= float(input('Digite o cateto oposto '))
adjacente= float(input('Digite o cateto adjacente '))
hipotenuza= math.sqrt(pow(oposto,2) + pow(adjacente,2))
print('A hipotenuza é {}'.format(hipotenuza))
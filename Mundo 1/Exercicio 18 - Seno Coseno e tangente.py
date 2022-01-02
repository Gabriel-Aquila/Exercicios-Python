import math
angulo = float(input('Digite o angulo '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno de {}° é {:.3f} , o coseno é {:.3f} e a tangente é {:.3f}'.format(
    angulo, seno, coseno, tangente))

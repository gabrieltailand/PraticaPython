import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print('\033[1;31mO ângulo {} tem o SENO {:.2f}\033[m'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('\033[1;34mO ângulo de {} tem o COSSENO de {:.2f}\033[m'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('\033[1;33mO ângulo de {} tem a TANGENTE de {:.2f}\033[m'.format(angulo, tangente))


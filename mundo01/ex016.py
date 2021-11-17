#import math
#num = float(input('Digite um número real: '))
#print('O número {} tem a parte inteira {}'.format(num, int(num)))

from math import trunc
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))



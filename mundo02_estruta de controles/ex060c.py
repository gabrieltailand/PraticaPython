numero = int(input('Digite um valor para ver seu fatorial: '))
fatorial = 1

for c in range(numero, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    fatorial *= c
print(fatorial)
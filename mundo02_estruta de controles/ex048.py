'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.'''

soma = 0 # Acumulador ( normamente soma 1 valor)
cont = 0 # Contador ( normalmente conta e soma 1)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos {} valores solicitados é {}'.format(cont, soma))

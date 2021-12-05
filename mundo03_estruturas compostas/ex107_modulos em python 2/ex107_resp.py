'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo 15%, temos R${moeda.diminuir(p, 15):.2f}')
print(f'Aumentando 5%, temos {moeda.moeda(preço)}')



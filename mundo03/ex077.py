'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas vogais.'''

palavras = ('Motivacao', "Esperanca", 'Virtude', 'Carinho', 'Amor', 'Paz', 'Reconhecimento', 'Alegria', 'Felicidade',
            'Paciencia', 'Bondade', 'Caridade', 'Compaixao', 'Benignidade', 'Dignidade', 'Empatia', 'Deus')

for p in palavras:
    print(f'\nA palavra {p.upper()} possui as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

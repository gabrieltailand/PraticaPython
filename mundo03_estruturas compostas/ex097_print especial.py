'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
--------------
Olá, Mundo!
--------------'''

def escreva(msg):
    caract = '-'
    tam = len(msg)
    print(caract * tam)
    print(msg)
    print(caract * tam)

while True:
    escreva(msg = str(input('Digite uma mensagem: ')))
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
print('FIM DO PROGRAMA!')

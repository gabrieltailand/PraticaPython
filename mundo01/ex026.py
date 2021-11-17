'''Faça um programa que leia uma frase pelo teclado e mostre:
- quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('\033[1;4;7mA letra "A" aparece {} vezes na frase acima\033[m'.format(frase.count('A')))
print('\033[1;4;7mA primeira letra A aparece na posição {}\033[m'.format(frase.find('A') + 1))
print('\033[1;4;7mA última letra A aparece na posição {}\033[m'.format(frase.rfind('A') + 1))




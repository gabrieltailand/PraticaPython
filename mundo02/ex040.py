'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no final, de acordo com
a média atingida.'''

nota1 = float(input('Digite a primeita nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi {}. Você está \033[1;31mREPROVADO\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}. Você está em \033[1;36mRECUPERAÇÃO\033[m'.format(media))
elif media >= 7.0:
    print('Sua média foi {}. Parabéns, você foi \033[1;34mAPROVADO\033[m'.format(media))
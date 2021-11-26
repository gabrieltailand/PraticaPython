with open('arquivo_test.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Esta é uma linha que eu escrevi usando python\n')
    arquivo.write('Esta é a segunda linha que eu escrevi usando python\n')
with open('arquivo_test.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')


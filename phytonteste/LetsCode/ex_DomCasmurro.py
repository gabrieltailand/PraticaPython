arquivo = open('DomCasmurro.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

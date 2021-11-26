Adicionar elemento:
lista.append(elemento) # adiciona elemento no final da lista
lista.insert(0, 'Elemento')

Apagar elementos:
del lista[] # indicar o indice que quer eliminar
lista.pop() # eliminar o ultimo elemento
lista.remove() # indicar o valor que quer remover. Pelo conteúdo.

#Criando lista a partir de um range, usando o for:
valores = list(range(4, 11)

#Colocando a lista em ordem crescente e decrescente.
valores.sort()
valores.sort(reverse=True)

# Tamanho de uma lista.
len(lista)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')

pessoas = list()
dados = list()
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso em Kg: ')))
    pessoas.append(dados[:])
    dados.clear()





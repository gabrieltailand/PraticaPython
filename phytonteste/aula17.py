# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# # num.pop(2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'esta lista tem {len(num)} elementos.')

# valores.append(5)
# valores.append(9)
# valores.append(4)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('-' * 30)
for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')
print('Final da lista.')
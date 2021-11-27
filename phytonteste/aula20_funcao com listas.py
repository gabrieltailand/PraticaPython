def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(f'Lista normal: {valores}')
dobra(valores)
print(f'Lista dobrada: {valores}')

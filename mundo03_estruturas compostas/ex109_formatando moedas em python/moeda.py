def aumentar(preço=0, taxa=0, formate=False):
    """
    Aumenta determinado preço a uma determinada taxa e mostra a formatação personalizada
    :param preço: preço a ser lido
    :param taxa: taxa percentual almejada
    :param formate: formata ou não o preço inserido
    :return: retorna um preço formatado ou não com um acréscimo a uma taxa desejada.
    """
    res = preço + (preço * taxa/100)
    return res if formate is False else moeda(res)


def diminuir(preço=0, taxa=0, formate=False):
    """
    Diminue determinado preço a uma determinada taxa e mostra a formatação personalizada
    :param preço: preço a ser lido
    :param taxa: taxa percentual almejada
    :param formate: formata ou não o preço inserido
    :return: retorna um preço formatado ou não com um decréscimo a uma taxa desejada.
    """
    res = preço - (preço * taxa/100)
    return res if formate is False else moeda(res)


def dobro(preço=0, formate=False):
    """
    O dobro de um determinado preço a uma determinada taxa e mostra a formatação personalizada
    :param preço: preço a ser lido
    :param formate: formata ou não o preço inserido
    :return: retorna o dobro de um determinado preço.
    """
    res = preço * 2
    return res if not formate else moeda(res)


def metade(preço=0, formate=False):
    """
    A metade de um determinado preço a uma determinada taxa e mostra a formatação personalizada
    :param preço: preço a ser lido
    :param formate: formata ou não o preço inserido
    :return: retorna a metade de um determinado preço.
    """
    res = preço / 2
    return res if not formate else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>5.2f}'.replace('.', ',')



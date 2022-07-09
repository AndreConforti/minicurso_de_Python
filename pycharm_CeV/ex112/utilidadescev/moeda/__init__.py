def aumentar(valor=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preco,
    retornando o resultado com ou sem formatação.
    :param valor: o preco que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formatação
    """
    res = valor + (valor * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - (valor * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if not formato else moeda(res)


def metade(valor=0, formato=False):
    res= valor / 2
    return res if not formato else moeda(res)


def moeda(valor=0, moeda='R$ '):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, taxaa=10, taxar=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço:  \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(valor, taxar, True)}')
    print('-' * 30)
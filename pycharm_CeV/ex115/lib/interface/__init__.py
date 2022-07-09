def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO: usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for pos, item in enumerate(lista):
        print(f'\033[0;33m{pos + 1}\033[m - \033[0;34m{item}\033[m')
    print(linha())
    opc = leiaInt('\033[0;32mSua opção: \033[m')
    return opc

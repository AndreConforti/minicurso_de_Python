'''Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também uma função leiaFloat(),
com a mesma funcionalidade.'''

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


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m\nERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('0\33[31m\nERRO: usuário preferiu não digitar.\033[m')
            return 0
        else:
            return f

numI = leiaInt('Digite um número inteiro: ')
numF = leiaFloat('Digite um número real: ')
print(f'Você digitou o número {numI} e o número {numF:.2f}')
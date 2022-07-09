'''Faça um nini-sistema que utilize o interactive help
do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra FIM, o programa
se encerrará. USE CORES'''
from time import sleep


cores = (
        '\033[m',         # 0 - sem cores
        '\033[0;37;40m',  # 1 - branco
        '\033[0;30;41m',  # 2 - vermelho
        '\033[0;30;42m',  # 3 - verde
        '\033[0;30;43m',  # 4 - amarelo
        '\033[0;30;44m',  # 5 - azul
        '\033[0;30;45m',  # 6 - roxo
        '\033[0;30;46m',  # 7 - turqueza
        '\033[7;30;47m'   # 8 - cinza
        )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[6], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 10
    print(cores[cor], end='')
    print('*' * tam)
    print(f'{msg.center(tam)}')
    print('*' * tam)
    print(cores[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    comando = str(input('Função ou Biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)

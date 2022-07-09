
'''Faça um programa que tenha uma função chamada notas() que
pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informaçãoes:
- Qiantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings'''

def notas(*n, sit=False):
    """
    ->Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoável'
        else:
            r['situacao'] = 'Ruim'
    return r


#Programa Principal
resp = notas(5.5, 4.5, 10, 8, sit=True)
print(resp)
help(notas)


'''Adicione ao módulo moeda.py criado nos desafios anteriores, uma
função chamada resumo(), que mostre na tela algumas informações
geradas pelas funções.'''

from utilidadescev import moeda, dado

preco = dado.leiaDinheiro('Digite o preço: R$ ')

moeda.resumo(preco, 20, 12)

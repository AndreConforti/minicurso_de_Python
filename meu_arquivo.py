# Definir essencialmente o que deve ser feito (Lógica do Programa)
# Importar bibliotecas------------------------------------------------------------------------------------------------
import pandas as pd

# Importar a base de dados--------------------------------------------------------------------------------------------
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a base de dados------------------------------------------------------------------------------------------
pd.set_option('display.max_columns', None)
#print(tabela_vendas)

# Faturamento por loja------------------------------------------------------------------------------------------------
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print('-' * 50)

# Quantidade de produtos vendidos por loja----------------------------------------------------------------------------
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-' * 50)

# Ticket Médio por produto em cada loja (Faturamento / Quantidade de produtos vendidos)-------------------------------
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()  #.to_frame transforma os dados em uma tabela
print(ticket_medio)

# Enviar um email com o relatório-------------------------------------------------------------------------------------


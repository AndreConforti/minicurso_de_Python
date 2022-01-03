# Definir essencialmente o que deve ser feito (Lógica do Programa)
# Importar bibliotecas------------------------------------------------------------------------------------------------
import pandas as pd
import win32com.client as win32

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
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})
print(ticket_medio)

# Enviar um email com o relatório-------------------------------------------------------------------------------------
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'gcm.martins.leme@gmail.com'
mail.Subject = 'Relatório de vendas por loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R$ {:,.2f}'.format})}

<p>Quantidade vendida:</p>
{quantidade.to_html()}

<p>Ticket médio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R$ {:,.2f}'.format})}

<p>Qualquer dúvida, estou à disposição.</p>

<p>Att,</p>
<p>André Conforti.</p>
'''

mail.Send()
print('email enviado')
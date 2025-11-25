import sqlite3

con = sqlite3.connect("banco_de_dados.db")
cursor = con.cursor()

consulta = cursor.execute(
    '''
    SELECT Max (Idade) FROM minha_tabela
    GROUP BY Nome
'''
)

for i in consulta:
    print(i)
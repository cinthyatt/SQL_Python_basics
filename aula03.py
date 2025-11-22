import sqlite3
from random import randint

conexao = sqlite3.connect("banco_de_dados.db")
cursor = conexao.cursor()

'''cursor.execute('CREATE TABLE IF NOT EXISTS minha_tabela(Data text, Nome text, Idade real )')

cursor.execute('INSERT INTO minha_tabela VALUES ("01/01/2021", "Odemir", 30)')
cursor.execute('INSERT INTO minha_tabela VALUES ("05/01/2021", "Lucas", 30)')

for _ in range(10):
    numero = randint(10,20)
    cursor.execute(f'INSERT INTO minha_tabela VALUES ("10/01/2021", "Lucas", {numero})')


consulta = cursor.execute("SELECT * FROM minha_tabela").fetchall()
for linha in consulta:
    print(linha)

conexao.commit()'''

'''consulta = cursor.execute("SELECT * FROM minha_tabela WHERE Nome<>'Odemir'and'Lucas'").fetchall()
print(consulta)'''

'''consulta = cursor.execute('SELECT * FROM minha_tabela WHERE idade BETWEEN 15 and 20')
for linha in consulta:
    print(linha)'''

'''consulta = cursor.execute("SELECT * FROM minha_tabela WHERE Nome LIKE 'A%'").fetchall()
for linha in consulta:
    print(linha)'''

'''consulta = cursor.execute("SELECT * FROM minha_tabela WHERE Nome LIKE 'a%a'").fetchall()
for linha in consulta:
    print(linha)'''

consulta = cursor.execute("SELECT * FROM minha_tabela WHERE Idade IN (15, 20, 30)").fetchall()
for linha in consulta:
    print(linha)
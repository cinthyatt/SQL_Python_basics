import sqlite3

con = sqlite3.connect("banco_de_dados.db")
cursor = con.cursor()

#consulta = cursor.execute('CREATE TABLE IF NOT EXISTS tab_vendas(id real, valor real)')
#consulta = cursor.execute('CREATE TABLE IF NOT EXISTS tab_cad_vendas(id real, nome text)')

'''cursor.execute("INSERT INTO tab_vendas VALUES (1, 100)")
cursor.execute("INSERT INTO tab_vendas VALUES (1, 200)")
cursor.execute("INSERT INTO tab_vendas VALUES (1, 150)")

cursor.execute("INSERT INTO tab_vendas VALUES (2, 50)")
cursor.execute("INSERT INTO tab_vendas VALUES (2, 200)")
cursor.execute("INSERT INTO tab_vendas VALUES (2, 900)")'''

#cursor.execute("INSERT INTO tab_cad_vendas VALUES (1, 'Odemir Jr')")
#cursor.execute("INSERT INTO tab_cad_vendas VALUES (2, 'Lucas Alves')")

#consulta = cursor.execute('SELECT * FROM tab_vendas INNER JOIN tab_cad_vendas ON tab_vendas.id = tab_cad_vendas.id')

#consulta = cursor.execute('INSERT INTO tab_vendas VALUES (3, 9999)')

consulta = cursor.execute('SELECT * FROM tab_vendas RIGHT JOIN tab_cad_vendas ON tab_vendas.id = tab_cad_vendas.id')

#consulta = cursor.execute("SELECT * FROM tab_vendas")
for i in consulta:
    print(i)

con.commit()

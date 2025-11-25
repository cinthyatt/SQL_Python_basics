import sqlite3

con = sqlite3.connect("banco_de_dados.db")
cursor = con.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS tabX (id real, nome text)')
#cursor.execute('CREATE TABLE IF NOT EXISTS tabY (id real, nome text)')

'''cursor.execute('INSERT INTO tabX VALUES (1, "Maria")')
cursor.execute('INSERT INTO tabX VALUES (2, "Jose")')
cursor.execute('INSERT INTO tabX VALUES (3, "Antonio")')

cursor.execute('INSERT INTO tabY VALUES (1, "Ana")')
cursor.execute('INSERT INTO tabY VALUES (2, "Elsa")')
cursor.execute('INSERT INTO tabY VALUES (3, "Cristoph")')'''

#consulta = cursor.execute('SELECT * FROM tabY').fetchall()
#print(consulta)

consulta = cursor.execute(
    ''' 
        SELECT * FROM tabX
        UNION ALL
        SELECT * FROM tabY

    '''
)

for i in consulta:
    print(i)

con.commit()
import sqlite3
from random import randint

conexao = sqlite3.connect("Banco de Dados")
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE minha_tabela(Data text, Nome text, Idade real )')
#conexao.commit()

#cursor.execute('INSERT INTO minha_tabela VALUES ("01/01/2021", "Odemir", 30)')
#cursor.execute('INSERT INTO minha_tabela VALUES ("05/01/2021", "Lucas", 30)')

'''for loop in range(10):
    numero = randint(10,20)
    cursor.execute(f'INSERT INTO minha_tabela VALUES ("10/01/2021", "Lucas", {numero})')'''



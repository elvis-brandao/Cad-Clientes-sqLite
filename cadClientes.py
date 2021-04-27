import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	cpf	VARCHAR(11) NOT NULL,
	email TEXT NOT NULL,
	fone TEXT,
	cidade TEXT,
	uf VARCHAR(2) NOT NULL);""")

##################################################
reg = 'S'
while reg == 'S':
    reg = input('Cadastrar um novo cliente? [S/N] ').strip().upper()
    while reg not in 'sSnN':
        reg = input('Cadastrar um novo cliente? [S/N] ').strip().upper()
    if reg == 'S':
        # solicitando os dados ao usuário
        p_nome = input('Nome: ')
        p_idade = input('Idade: ')
        p_cpf = input('CPF: ')
        p_email = input('Email: ')
        p_fone = input('Fone: ')
        p_cidade = input('Cidade: ')
        p_uf = input('UF: ')

        # inserindo dados na tabela
        cursor.execute("""INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf)
        VALUES (?,?,?,?,?,?,?)""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf))

        conn.commit()

        print('Dados inseridos com sucesso.')
        print('<>' * 30)
    else:
        break
##################################################
# lendo os dados
print('\nOs dados salvos na base de dados são:')

cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)
##################################################    
# desconectando...
conn.close()

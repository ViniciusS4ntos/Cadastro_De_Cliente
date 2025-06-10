from conexao import conectar

nome = input("Nome: ").title()
email = input("Email: ")
telefone = input("Telefone: ")

conn = conectar()
cursor = conn.cursor()
cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
conn.commit()
cursor.close()
conn.close()

print("Cliente cadastrado com sucesso!")

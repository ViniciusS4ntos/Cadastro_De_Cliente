import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        # Tenta conectar ao banco
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cadastro_clientes"
        )
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco não encontrado. Criando banco...")

            # Conecta sem especificar o banco
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE cadastro_clientes DEFAULT CHARACTER SET 'utf8'")
            cursor.close()
            conn.close()
            print("Banco criado com sucesso!")

            # Agora conecta ao novo banco
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cadastro_clientes"
            )

            # Cria tabela se não existir
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100),
                    telefone VARCHAR(20)
                )
            """)
            conn.commit()
            cursor.close()

            return conn
        else:
            raise

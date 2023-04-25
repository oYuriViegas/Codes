import getpass
import oracledb

pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="YuriUser",
    password=pw,
    dsn="localhost/xe")

print("Successfully connected to Oracle Database")

#O cursor é um objeto criado usando a conexão estabelecida com o bd, ele permite executar consultas SQL no banco de dados
cursor = connection.cursor()

#Executando a consulta SQL na tabela "Amostras"
cursor.execute("SELECT * FROM Amostras")

#Usando o método "fetchall()" o cursor lê todos os resultados da consulta e armazena os dados na variável "dadosRecebidos"
dadosRecebidos = cursor.fetchall()

#Imprimindo os resultados
print(dadosRecebidos)

#Fechando o cursor e a conexão
cursor.close()
connection.close()

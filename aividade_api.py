import requests
import mysql.connector

cep = input("Digite o Cep para consulta: ")

while cep.__len__() != 8:
    print('Digite Um cep valido de 8 Digitos: ')
    cep = input("Digite Cep: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)
dados = resposta.json()

if resposta.status_code == 200:
   
    print(f"Cep: {dados['cep']}")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Complemento: {dados['complemento']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Estado: {dados['estado']}")
    print(f"Localidade: {dados['localidade']}")

else:
    print(f"Deu Erro {resposta.status_code} ")


conexao = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost',
    database = 'cep_teste2'

)

mysql =  """
    INSERT INTO cep_1 (cep, logradouro, complemento, bairro, estado, localidade)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

valores = valores = (
        dados['cep'],
        dados['logradouro'],
        dados['complemento'],
        dados['bairro'],
        dados['estado'],
        dados['localidade']
    )
cursor = conexao.cursor()

cursor.execute(mysql,valores)

conexao.commit()

print('Dados salvos!')
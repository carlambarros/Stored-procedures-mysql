import os
import mysql.connector
from dotenv import load_dotenv


# carrega as variáveis do arquivo .env
load_dotenv()

# Conexão
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
)

# Criando o cursor padrão
cursor = conexao.cursor()

# Função para exibir a tabela
def exibir_tabela(colunas, dados):
    tamanhos = []
    for i, coluna in enumerate(colunas):
        maior = len(str(coluna))
        for linha in dados:
            if len(str(linha[i])) > maior:
                maior = len(str(linha[i]))
        tamanhos.append(maior)
        
    linha_divisoria = "+"
    for tamanho in tamanhos:
        linha_divisoria += "-" * (tamanho + 2) + "+"
    print(linha_divisoria)
    
    cabecalho = "|"
    for i, coluna in enumerate(colunas):
        cabecalho += f" {coluna.ljust(tamanhos[i])} |"
    print(cabecalho)
    print(linha_divisoria)
    
    for registro in dados:
        linhas_dados = "|"
        for i, valor in enumerate(registro):
            linhas_dados += f" {str(valor).ljust(tamanhos[i])} |"
        print(linhas_dados)
    print(linha_divisoria)
   
# Cadastrar produto
def cadastrar_produto():
    try:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        cursor.callproc("Cadastrar_Produto", [nome, preco])
        conexao.commit()
        print("Produto cadastrado com sucesso")
    except Exception as erro:
        print("\nErro:", erro)
    print("\n" + "=" * 50)
   
# Selecionar produtos
def listar_produtos():
    try:
        quantidade = int(input("Quantos produtos deseja listar? "))
        cursor.callproc("Selecionar_Produtos", [quantidade])
        
        # Captura o primeiro conjunto de resultados real gerado pela procedure
        resultado = next(cursor.stored_results())
        dados = resultado.fetchall()
        
        if dados:
            colunas = [desc[0] for desc in resultado.description]
            print("\nProdutos Encontrados: \n")
            exibir_tabela(colunas, dados)
        else:
            print("\nNenhum produto encontrado")
                
    except StopIteration:
        print("\nA procedure não retornou nenhuma tabela de dados.")
    except Exception as erro:
        print("\nErro:", erro)
    print("\n" + "=" * 50)

# Contar produtos
def contar_produtos():
    try: 
        retorno = cursor.callproc("Contar_Produtos", [0])
        
        if retorno:
            print(f"\nQuantidade de Produtos: {retorno[0]}")
        else:
            print("Nenhum produto encontrado em estoque")
                
    except Exception as erro:
        print("\nErro:", erro)
    print("\n" + "=" * 50)
        
# Buscar Produto    
def buscar_produto():
    try:
        nome = input("Qual produto você deseja buscar? ")
        cursor.callproc("Buscar_Produto", [nome])
        
        resultado = next(cursor.stored_results())
        dados = resultado.fetchall()
        
        if dados:
            colunas = [desc[0] for desc in resultado.description]
            print("\nProdutos Encontrados com este nome: \n")
            exibir_tabela(colunas, dados)
        else:
            print("\n Nenhum produto encontrado")
                
    except StopIteration:
        print("\nA procedure não retornou nenhuma tabela de dados.")
    except Exception as erro:
        print("\nErro:", erro)
    print("\n" + "=" * 50)
 
# Menu
while True:
    print("\n========================")
    print("Sistema de estoque TADS24")
    print("1-Cadastrar produto")
    print("2-Listar produtos")
    print("3-Contar Produtos")
    print("4-Buscar Produto")
    print("0-Sair")
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        contar_produtos()
    elif opcao == "4":
        buscar_produto()
    elif opcao == "0":
        print("Sistema Encerrado")
        break
    else:
        print("\nOpção inválida")
        print("\n" + "=" * 50)

# Fechando conexão
cursor.close()
conexao.close()

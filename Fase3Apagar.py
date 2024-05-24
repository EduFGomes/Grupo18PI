import getpass
import cx_Oracle

def conectar_banco():
    pw = getpass.getpass("Insira a senha:")
    try:
        conexao = cx_Oracle.connect(
            user="BD150224333",
            password=pw,
            dsn='BD-ACD/xe')
        print("Conectado ao banco de dados Oracle:", conexao.version)
        return conexao
    except cx_Oracle.Error as erro:
        print("Erro ao conectar:", erro)
        return None

def apagar_produto_por_nome(cursor, nome_produto):
    try:
        cursor.execute("DELETE FROM tabela_produtos WHERE nome = :nome_produto", {'nome_produto': nome_produto})
        print("Produto", nome_produto, "foi removido.")
    except cx_Oracle.Error as error:
        print("Erro ao apagar produto:", error)

def apagar_produto_por_codigo(cursor, codigo_produto):
    try:
        cursor.execute("SELECT nome FROM tabela_produtos WHERE codigo_prod = :codigo_produto", {'codigo_produto': codigo_produto})
        nome_produto = cursor.fetchone()[0]
        confirmacao = input("Tem certeza que deseja remover o produto '{}' com o código {}? (Sim/Não): ".format(nome_produto, codigo_produto)).lower()
        if confirmacao == "sim":
            cursor.execute("DELETE FROM tabela_produtos WHERE codigo_prod = :codigo_produto", {'codigo_produto': codigo_produto})
            print("Produto", nome_produto, "de código", codigo_produto, "foi removido.")
        else:
            print("Operação cancelada.")
    except cx_Oracle.Error as error:
        print("Erro ao apagar produto:", error)

def apagar_todos_produtos(cursor):
    try:
        confirmacao = input("Tem certeza que deseja remover todos os produtos? (Sim/Não): ").lower()
        if confirmacao == "sim":
            cursor.execute("DELETE FROM tabela_produtos")
            print("Todos os produtos foram removidos.")
        else:
            print("Operação cancelada.")
    except cx_Oracle.Error as error:
        print("Erro ao apagar produtos:", error)

def main():
    
    connection = conectar_banco()
    if connection:
        cursor = connection.cursor()
       
        print("Opções de remoção de produto:")
        print("1. Remover pelo nome do produto")
        print("2. Remover pelo código do produto")
        print("3. Remover todos os produtos")
        opcao = input("Escolha a opção desejada (1, 2 ou 3): ")
        
        if opcao == "1":
            produto_nome = input("Digite o nome do produto que deseja remover: ")
            confirmacao = input("Tem certeza que deseja remover o produto '{}' ? (Sim/Não): ".format(produto_nome)).lower()
            if confirmacao == "sim":
                apagar_produto_por_nome(cursor, produto_nome)
            else:
                print("Operação cancelada.")
        
        elif opcao == "2":
            try:
                produto_codigo = int(input("Digite o código do produto que deseja remover: "))
                apagar_produto_por_codigo(cursor, produto_codigo)
            except ValueError:
                print("Por favor, digite um número inteiro válido para o código do produto.")
        
        elif opcao == "3":
            apagar_todos_produtos(cursor)
        
        else:
            print("Opção inválida.")
        
        connection.commit()
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()

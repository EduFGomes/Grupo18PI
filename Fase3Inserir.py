import getpass
import oracledb

def inserir(cod, Inome, Idescricao, Icp, Icf, Icv, Iiv, Iml):
    cursor.execute(f"""insert into tabela_produtos (codigo_prod, nome, descricao, custo_prod, custo_fixo, comissao_venda, impostos, rentabilidade)
    values ({cod}, '{Inome}', '{Idescricao}', {Icp}, {Icf}, {Icv}, {Iiv}, {Iml})""")

quant = int(input('Quantos itens deseja inserir? '))
for i in range(quant):
    try:
        conexao = oracledb.connect(
        user = "BD150224325",
        password = "Rpotd1",
        dsn = 'BD-ACD/xe')
    except Exception as erro:
        print("Erro ao conectar", erro)
    else:
        print("Conectado", conexao.version)
        cursor = conexao.cursor()
    
        cursor.execute("""select distinct codigo_prod from tabela_produtos""")
        tabela = cursor.fetchall()

        print(f'{i+1}° Item: ')
        cod = (len(tabela) + 1)
        Inome = input("Nome do produto: ")
        Idescricao = input("Descrição: ")
        Icp = float(input("Custo do produto: "))
        Icf = int(input("Custo fixo: "))
        Icv = int(input("Comissão de venda: "))
        Iiv = int(input("Impostos: "))
        Iml = int(input("Margem de lucro: "))

        if(Icf + Icv + Iiv + Iml) < 100:
            inserir(cod, Inome, Idescricao, Icp, Icf, Icv, Iiv, Iml)
            print('Item inserido com sucesso!')
        else:
            print("Não é possível inserir na tabela, pois a soma das porcentagens não pode ser maior ou igual a 100%")
    
        conexao.commit()

        cursor.close
        conexao.close

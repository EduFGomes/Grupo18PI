import getpass
import oracledb

def multip(matriz, pares):
    return [
        (matriz[0][0] * pares[0] + matriz[0][1] * pares[1]) % 26,
        (matriz[1][0] * pares[0] + matriz[1][1] * pares[1]) % 26
    ]

def criptografia(texto, chave):
    texto = texto.replace(" ", "").lower()
    if len(texto) % 2 != 0:
        texto += texto[-1]
    pares = []
    for i in range(0, len(texto), 2):
        p1 = cifra_hill.index(texto[i])
        p2 = cifra_hill.index(texto[i+1])
        pares.append([p1, p2])
    cripto = ""
    for par in pares:
        a = multip(chave, par)
        cripto += cifra_hill[a[0]] + cifra_hill[a[1]]
    
    return cripto

def descriptografia(cripto): 
    pares = []
    for i in range(0, len(cripto), 2):
        p1 = cifra_hill.index(cripto[i])
        p2 = cifra_hill.index(cripto[i+1])
        pares.append([p1, p2])
    descripto = ""
    for par in pares:
        b = multip(chaveinv, par)
        descripto += cifra_hill[b[0]] + cifra_hill[b[1]]
    return descripto

def inserir(cod, Inome, Idescricao, Icp, Icf, Icv, Iiv, Iml):
    cursor.execute(f"""insert into tabela_produtos (codigo_prod, nome, descricao, custo_prod, custo_fixo, comissao_venda, impostos, rentabilidade)
    values ({cod}, '{Inome}', '{Idescricao}', {Icp}, {Icf}, {Icv}, {Iiv}, {Iml})""")
       
def apagar():
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
            print("Digite um número inteiro válido para o código do produto.")
        
    elif opcao == "3":
        apagar_todos_produtos(cursor)
        
    else:
        print("Opção inválida.")
        
    conexao.commit()

def alterar():   
    def tela_alteracao():
        print ('\n', "-"*90, '\n')
        print (" "*25 , 'BEM VINDO AO MENU DE ALTERAÇÃO')
        print ('\n', "-"*90, '\n')
        
        
    def navegarAlteracoes(tela_atualA):
        while True:
            telas[tela_atualA]()
            resposta = str (input ('Deseja alterar algo? \n[SIM] ou [NAO]\n'))
            if resposta.lower() == 'sim':
                print ('Para alterar valores de uma coluna específica - digite "1"')
                print ('Para alterar o nome de uma coluna específica - digite "2"')
                escolha = int(input('digite o número desejado: '))
                if escolha == 1:
                    tela_atualA = 'Avalores'
                elif escolha == 2:
                    tela_atualA = 'Anome'
                else:
                    print ('tela não reconhecida, tente novamente')
            if resposta.lower() == 'nao':
                print ('voltando ao menu')
                
    def tela_Avalores():
        print("TELA DE ALTERAÇÃO DE VALORES")
        Avalor_antigo = str (input ('Nome antigo (igual escrito na tabela): '))
        Avalor_novo = str (input ('Nome novo: '))
        Acoluna = str (input ('Nome da coluna: '))
        cursor.execute (f"""
                        update tabela_produtos 
                        set {Acoluna} = '{Avalor_novo}'
                        where {Acoluna} = '{Avalor_antigo}'
                        """)                     
        conexao.commit()
        print ('Valor atualizado com sucesso!')

    def tela_Anome():
        print("TELA DE ALTERAÇÃO DE NOME")
        Anome_antigo = str (input ('Nome antigo da coluna(igual escrito na tabela): '))
        Anome_novo = str (input ('Nome novo da coluna: '))
        cursor.execute (f"""
                        ALTER TABLE tabela_produtos 
                        RENAME COLUMN {Anome_antigo} to {Anome_novo} 
                        """)
        conexao.commit()
        print ('Nome da coluna atualizado com sucesso!')
    

    telas = {'menu alteracao' : tela_alteracao,
            'Avalores': tela_Avalores,
            'Anome': tela_Anome,
            'navegar alteracoes':navegarAlteracoes
            }

    def mainAlteracoes():
        tela_atualA = 'menu alteracao'
        navegarAlteracoes (tela_atualA)

    mainAlteracoes()

def listar():
    cursor.execute("""select distinct codigo_prod from tabela_produtos""")
    tabela = cursor.fetchall()

    for cod in range (1, len(tabela)+1):
        cursor.execute(f"""select NOME from tabela_produtos where codigo_prod = {cod}""")
        nome = cursor.fetchall()
        cursor.execute(f"""select DESCRICAO from tabela_produtos where codigo_prod = {cod}""")
        descricao = cursor.fetchall()
        cursor.execute(f"""select CUSTO_PROD from tabela_produtos where codigo_prod = {cod}""")
        cp = cursor.fetchall()
        cursor.execute(f"""select CUSTO_FIXO from tabela_produtos where codigo_prod = {cod}""")
        cf = cursor.fetchall()
        cursor.execute(f"""select COMISSAO_VENDA from tabela_produtos where codigo_prod = {cod}""")
        cv = cursor.fetchall()
        cursor.execute(f"""select IMPOSTOS from tabela_produtos where codigo_prod = {cod}""")
        iv = cursor.fetchall()
        cursor.execute(f"""select RENTABILIDADE from tabela_produtos where codigo_prod = {cod}""")
        ml = cursor.fetchall()
        pv = cp[0][0] / (1 - ((cf[0][0] + cv[0][0] + iv[0][0] + ml[0][0])/100))
    
        if(pv<=0):
            print('-'*45)
            print(f'Preço de venda menor ou igual a zero -> {pv}')
        else:
            print('-'*45)
            print("Código do produto:", cod)
            print("Nome do produto:", nome[0][0])
            print(f"Descrição o produto: {descriptografia(Idescricao)}\n")
            print(f"Descrição                      {'Valor':6} | {'  %':6}")
            print(f"A. Preço de venda              {pv:6.2f} | {'   100%':6}")
            print(f"B. Custo de aquisição          {cp[0][0]:6.2f} | {(cp[0][0] * 100) / pv:6.2f}%")
            print(f"C. Receita Bruta               {pv - cp[0][0]:6.2f} | {100 - ((cp[0][0] * 100) / pv):6.2f}%")
            print(f"D. Custo fixo/Administrativo   {(pv * cf[0][0]) / 100:6.2f} | {cv[0][0]:6.2f}%")
            print(f"E. Comissão de vendas          {(pv * cv[0][0]) / 100:6.2f} | {cv[0][0]:6.2f}%")
            print(f"F. Impostos                    {(pv * iv[0][0]) / 100:6.2f} | {iv[0][0]:6.2f}%")
            print(f"G. Outros custos               {((pv * cf[0][0]) / 100) + ((pv * cv[0][0]) / 100) + ((pv * iv[0][0]) / 100):6.2f} | {(cf[0][0] + cv[0][0] + iv[0][0]):6.2f}%")
            print(f"H. Rentabilidade               {(pv * (ml[0][0] / 100)):6.2f} | {(ml[0][0]):6.2f}%")

            if(ml[0][0]>20):
                print('-'*45)
                print('Lucro alto')
            elif(ml[0][0] > 10 and ml[0][0]<=20):
                print('-'*45)
                print('Lucro médio')
            elif(ml[0][0] > 0 and ml[0][0]<=10):
                print('-'*45)
                print('Lucro baixo')
            elif(ml[0][0]==0):
                print('-'*45)
                print('Equilíbrio')
            elif(ml[0][0]<0):
                print('-'*45)
                print('Prejuízo')
                print('-'*45)

try:
    conexao = oracledb.connect(
    user = "TESTE",
    password = "teste",
    dsn = 'localhost/XEPDB1')
except Exception as erro:
    print("Erro ao conectar", erro)
else:
    print("Conectado", conexao.version)
    cursor = conexao.cursor()

cifra_hill = "abcdefghijklmnopqrstuvwxyz"
chave = [[4, 3], [1, 2]]
chaveinv = [[42, -63],[-21, 84]]

escolha = 1
while escolha != 0:
    escolha = int(input('O que deseja fazer?\n[1] Inserir Produtos\n[2] Remover Produtos\n[3] Alterar Produtos\n[4] Listar Produtos\n[0] Sair\n:'))
    if escolha == 1:
        cursor.execute("""select distinct codigo_prod from tabela_produtos""")
        tabela = cursor.fetchall()
        quant = int(input('Quantos itens deseja inserir? '))
        for i in range(quant):
            print(f'{i+1}° Item: ')
            cod = (len(tabela) + 1)
            Inome = input("Nome do produto: ")
            Idescricao = input("Descrição: ")
            Idescricao = criptografia(Idescricao, chave)
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
    elif escolha == 2:
        apagar()
    elif escolha == 3:
        alterar()
    elif escolha == 4:
        listar()
    elif escolha == 0:
        print('Saindo...')
    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')
print('Fim do Programa.')

cursor.close()
conexao.close()

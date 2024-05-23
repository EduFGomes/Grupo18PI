#menu calteracao de valores 
import getpass
import oracledb

try:
    conexao = oracledb.connect(
    user = "BD150224132",
    password = "Crcud6",
    dsn = 'BD-ACD/xe')
except Exception as erro:
    print("Erro ao conectar", erro)
else:
    print("Conectado", conexao.version)
    cursor = conexao.cursor()
    
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
            #colocar menu geral 
                
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

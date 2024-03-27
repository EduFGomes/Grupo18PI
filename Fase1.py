cod_produto = int(input("Digite o código do produto: "))
nome_produto = input("Digite o nome do produto: ")
desc_produto = input("Digite a descrição do produto: ")
cp = float(input("Digite o custo do produto: "))
cf = float(input("Digite o custo fixo: "))
cv = float(input("Digite a comissão de venda: "))
iv = float(input("Digite a porcentagem de impostos: "))
ml = float(input("Digite a margem de lucro estipulada: "))

pv = cp / (1 - ((cf + cv + iv + ml)/100))
lucro_real = ml
lucro_pcpv = pv / cp - 100

if(pv<=0):
    print('-'*45)
    print(f'Preço de venda menor ou igual a zero -> {pv}')
else:
    print('-'*45)
    print(f"Descrição                      {'Valor':6} | {'  %':6}")
    print(f"A. Preço de venda              {pv:6.2f} | {'   100%':6}")
    print(f"B. Custo de aquisição          {cp:6.2f} | {(cp * 100) / pv:6.2f}%")
    print(f"C. Receita Bruta               {pv - cp:6.2f} | {100 - ((cp * 100) / pv):6.2f}%")
    print(f"D. Custo fixo/Administrativo   {(pv * cf) / 100:6.2f} | {cf:6.2f}%")
    print(f"D. Custo fixo/administrativo   {cf:6.2f} | {(cf * 100) / pv:6.2f}%")
    print(f"E. Comissão de vendas          {cv:6.2f} | {(cv * 100) / pv:6.2f}%")
    print(f"F. Impostos                    {iv:6.2f} | {(iv * 100) / pv:6.2f}%")
    print(f"G. Outros custos               {cf + cv + iv:6.2f} | {((cf + cv + iv) * 100) / pv:6.2f}%")
    print(f"H. Rentabilidade               {(pv - cp) - (cf + cv + iv):6.2f} | {(cv * 100) / pv:6.2f}%")
    
    if(((cv * 100) / pv)>20):
        print('-'*45)
        print('Lucro alto')
    elif(10<((cv * 100) / pv)<=20):
        print('-'*45)
        print('Lucro médio')
    elif(0<((cv * 100) / pv)<=10):
        print('-'*45)
        print('Lucro baixo')
    elif(((cv * 100) / pv)==0):
        print('-'*45)
        print('Equilíbrio')
    elif(((cv * 100) / pv)<0):
        print('-'*45)
        print('Prejuízo')
print('-'*45)
    

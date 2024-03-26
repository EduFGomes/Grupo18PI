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

print(f"Descrição                      Valor  %")
print(f"A. Preço de venda              {pv}    100%")
print(f"B. Custo de aquisição          {cp}    {(cp * 100) / pv}%")
print(f"C. Receita Bruta               {pv - cp}    {100 - ((cp * 100) / pv)}%")
print(f"D. Custo fixo/Administrativo   {(pv * cf) / 100}    {cf}%")
print(f"D. Custo fixo/administrativo   {cf}    {(cf * 100) / pv}%")
print(f"E. Comissão de vendas          {cv}    {(cv * 100) / pv}%")
print(f"F. Impostos                    {iv}    {(iv * 100) / pv}%")
print(f"G. Outros custos               {cf + cv + iv}    {((cf + cv + iv) * 100) / pv}%")
print(f"H. Rentabilidade               {(pv - cp) - (cf + cv + iv)}    {(cv * 100) / pv}%")

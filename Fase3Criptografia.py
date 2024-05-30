cifra_hill = "abcdefghijklmnopqrstuvwxyz"
chave = [[4, 3], [1, 2]]
chaveinv = [[42, -63],[-21, 84]]

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

texto = input("insira a mensagem a ser criptografada: ")
texto_cripto = criptografia(texto, chave)
print('texto criptografado:', texto_cripto)
texto_descripto = descriptografia(texto_cripto)
print('texto descriptografado:', texto_descripto)

cifra_hill = "abcdefghijklmnopqrstuvwxyz"
chave = [[4, 3], [1, 2]]

def multip(matriz, pares):
    return [
        (matriz[0][0] * pares[0] + matriz[0][1] * pares[1]) % 26,
        (matriz[1][0] * pares[0] + matriz[1][1] * pares[1]) % 26
    ]


def criptografia(cifra_hill, texto, chave):
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

texto = input("insira a mensagem a ser criptografada:")
textocripto = criptografia(texto, chave)
print('texto criptografado:', textocripto)

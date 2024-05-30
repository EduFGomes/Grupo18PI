def inv(matriz):
    det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = det % 26
    invdet = 1
    
    for i in range(26):
        if (det * i) % 26 == 1:
            invdet = i
            break
    
    matrizinv = [
        [matriz[1][1] * invdet % 26, -matriz[0][1] * invdet % 26],
        [-matriz[1][0] * invdet % 26, matriz[0][0] * invdet % 26]
    ]
    
    for i in range(2):
        for j in range(2):
            matrizinv[i][j] = matrizinv[i][j] % 26
    
    return matrizinv

def descripto(textocripto, chave):
    lista = convr(textocripto)
    chaveinv = inv(chave)
    texto = ""
    for par in lista:
        multip = matrz(chaveinv, [[par[0]], [par[1]]])
        texto += chr(multip[0][0] + 97) + chr(multip[1][0] + 97)
    return texto

nome = input('Insira uma frase: ')

textocripto = cripto(nome, matriz_cod)
print("Texto cifrado:", textocripto)

textodescripto = descripto(textocripto, matriz_cod)
print("Texto descriptografado:", textodescripto)

print(convr(nome))

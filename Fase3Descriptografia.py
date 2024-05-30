cifra_hill = "abcdefghijklmnopqrstuvwxyz"
chaveinv = [[42, -63],[-21, 84]]

def descriptografia(cripto, cifra_hill, chaveinv): 
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

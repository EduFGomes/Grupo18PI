#DECLARAÇÃO DE MATRIZES
cifra_hill = {'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5, 'f': 6,'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 0}
matriz_cod = [[1, 2], [3, 4]]
nome = [['c', 'n', 't'], ['a', 'e', 'a']]
P = []
C = []
#DEFINIÇÂO DA MATRIZ EMPARELHADA P
for i in range(len(nome)):
    P.append([])
    for j in range(len(nome[i])):
        P[i].append(cifra_hill[nome[i][j]])
print(P)
#MULTIPLICAÇÂO DE matriz_cod POR P (C)
for i in range(len(matriz_cod)):
    t1 = 0
    t2 = 0
    t3 = 0
    C.append([])
    if(i == 0):
        for j in range(len(matriz_cod[i])):
            t1 += matriz_cod[i][j] * P[j][i]
            t2 += matriz_cod[i][j] * P[j][i+1]
            t3 += matriz_cod[i][j] * P[j][i+2]
    else:
        for j in range(len(matriz_cod[i])):
            t1 += matriz_cod[i][j] * P[j][i-1]
            t2 += matriz_cod[i][j] * P[j][i]
            t3 += matriz_cod[i][j] * P[j][i+1]
    C[i].append(t1)
    C[i].append(t2)
    C[i].append(t3)
print(C)


#TESTES COM A BIBLIOTECA NUMPY

#TESTES COM A BIBLIOTECA NUMPY

#DECLARAÇÃO DE MATRIZES
import numpy as np
cifra_hill = {'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5, 'f': 6,'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 0}
matriz_cod = np.array([[1, 2], [3, 4]])
nome = np.array([['c', 'n', 't'], ['a', 'e', 'a']])
P = []
C = []
#DEFINIÇÂO DA MATRIZ EMPARELHADA P
for i in range(len(nome)):
    P.append([])
    for j in range(len(nome[i])):
        P[i].append(cifra_hill[nome[i][j]])
P = np.matrix(P)
print(P)
#MULTIPLICAÇÂO DE matriz_cod POR P (C)
C.append(np.dot(matriz_cod, P))
print(C)
#MODULAGEM
C = np.mod(C, 26)
print(C)
#DEFINIÇÃO DA MATRIZ CRIPTOGRAFADA
C = np.reshape(C, (1, np.size(C)))
print(C)
X = []
for i in range(np.size(C)):
    X.append('')
for i in cifra_hill:
    for j in range(np.size(C)):
        if cifra_hill[i] == C[0][j]:
            X[j] = i
print(X)
for i in range(len(X)):
    print(X[i], end='')
X = np.matrix(X)
print('\n', X)
X = np.reshape(X, (2, 3))
print(f'\n\n{nome}\n\n{X}')

import numpy as np

# Ex 1-5

n = 123
print(n)
numal = n
numal += 5
print(numal)
print(type(n))
n1 = float(n)
print(n1, type(n1), type(n))


# Ex 7-17
v = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(v[5])
v[7] = 100
print(v[1::2])
print(v[0::2])
inv1 = v[::-1]
print(inv1)
inv2 = inv1[2:7]
lin1 = v[::2]
print(lin1)
lin2 = lin1[::-1]
print(lin2)

print(v[7:2:-1])
print(v[2:7:-1])


# Ex 18-21
v100 = np.arange(1, 101, 1)
print(v100)

par100 = v100[1::2]
print(par100)
impar100 = v100[0::2]
print(impar100)

lincem = np.zeros
print(lincem)

lincem[0::2] = impar100
print(lincem)

lincem[1::2] = par100
print(lincem)


# Matrizes
# Ex 1-10
A = np.array([[0, 2, 4, 6], [1, 3, 5, 7], [9, 10, 11, 12]])
print(np.shape(A))
print('\n A = \n', A)

B = A[1, 1]
print('\n B = \n', B)

A[2, 1] = 10  # Elemento na 3 linha da primeira coluna passa a ter valor 10
print('\n A = \n', A)

C = A[1, :]  # Procura a segunda linha (0 é a primeira linha)
print('\n C = \n', C)

D = np.transpose(A[:, 1], 0)
# Ao fazer a transposta da matriz A, as linhas ficam colunas e as colunas ficam linhas
print('\n D = \n', D)


E = A[1:3, 1:3]
print('\n E = \n', E)

F = A[::-1, :]
print('\n F = \n', F)


G = A[:, ::-1]
"""   
      |   |
      V   |-> Vai correr do fim para o incio, devio ao "step" (passo) ser -1
      Corre do inicio ao fim, de forma normal
"""
print('\n G = \n', G)

H = A[1::2, 1::2]
print('\n H = \n', H)


print(' Dimensão de A: ', np.shape(A))
print(' Dimensão de C: ', np.shape(C))
print(' Dimensão de D: ', np.shape(D))

#Ex 11-17
vlin = A.flatten()
print(np.shape(vlin))
print('vlin = ', vlin)

I = A.transpose()
print(np.shape(I))
print('I = \n', I)

Z = np.zeros((6, 8), int)
print(np.shape(I), type(Z))
print('Z = \n', Z)

Z[1::2, 1::2] = A
print('Z = \n', Z)

Z[0::2, 0::2] = A
print('Z = \n', Z)

Z[1::2, 0::2] = A
print('Z = \n', Z)

Z[0::2, 1::2] = A
print('Z = \n', Z)

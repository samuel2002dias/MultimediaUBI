import matplotlib.pyplot as plt
import numpy as np
import math
num = 12345
print(num)

numalt = num
print(numalt)
print(type(num))

numf = 1.5
print(type(numf))

nome = 'Multimedia'
print(type(nome))

verdade = True
print(type(verdade))

nome = input('Qual o nome desta UC? ')
print('Bem vindo a ', nome)
print('Bem vindo a ' + nome)

nota1 = input('Qual nota do primeiro teste? ')
nota2 = input('Qual nota do primeiro teste? ')
print(type(nota1))

print('Nota final: ', float(nota1) + float(nota2))

texto_grande = '''
ergeg
ererv
erverv
'''
print(texto_grande)

texto = "também podem usar aspas, até porque podem querer usar ' no texto a escrever, ou vice-versa"
print(texto)

tt = "ss'a"
tt1 = 'aa"aa'
tt2 = tt+tt1

print(tt, '\n', tt1, '\n', tt2)

print(texto)
print(texto[0])
print(texto[-1])
print(texto[0:3])

novo = texto[29:35]
print(novo)
print(novo[4:])
print(novo[:-2])

print(len(texto))
print(texto.upper())
print(texto.find('p'))

print(2*3)
print(2+3)
print(5/2)
print(5//2)
print(5 % 2)
print(5 ** 2)
print(round(2.6))
print(abs(-2))


print(math.ceil(2.3))
outro = math.sqrt(9)
print(outro)

is_hot = False
is_cold = False
if is_hot == True:
    print("It's a hot day")
    print('Drink plenty of water ')
elif is_cold == True:
    print("It's a cold day")
    print('Drink plenty of water ')
else:
    print('Enjoy your  day')

if 2 > 3 or 3 > 2:
    print('obvio')
else:
    print('nunca')

if 2 > 3 and 3 > 2:
    print('obvio')
else:
    print('nunca')

if not 2 > 3 and 3 > 2:
    print('obvio')
else:
    print('nunca')

"""# Exercícios

1. Defina uma variável num contendo o seu número de aluno.
2. Crie uma nova variável numalt contendo o valor da sua variável num.
3. Some 5 ao valor da sua variável numalt .
4. Verifique o tipo da sua variável (num).
5. Altere o tipo da sua variável (num ) para float.
6. Verifique o valor e o tipo da sua variável num.

# Solução
"""

num = 12345
print(num)
numalt = num
numalt += 5
print(numalt)
print(type(num))
num = float(num)
print(num, type(num))

"""# Listas"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(lista))
print(lista)

print(lista[0:5])

print(lista[0:5:2])  # Começa na posição 0, acaba na posição 5, salta de 2 em 2

print(lista)
print(lista[::-1])


listas = np.concatenate((lista, lista[::-1]))
print(listas)

"""# Exercícios

7. Crie um vetor coluna vcol com 10 números à sua escolha.
8. Visualize o valor que está na posição 5 do seu vetor vcol.
9. Altere o valor da posição 7 do seu vetor vcol para 100.
10. Visualize os valores do seu vetor que se encontram nas posições pares.
11. Visualize os valores do seu vetor que se encontram nas posições ímpares.
12. Crie outro vetor coluna vcolinv1 contendo os valores do seu vetor vcol, mas por ordem inversa.
13. Crie outro vetor coluna vcolinv2 contendo os valores do seu vetor vcolinv1, que se encontram entre as posições 2 e 7.
14. Crie um vetor linha vlin1 com os valores do seu vetor vcol que se encontram nas posições pares.
15. Crie um vetor linha vlin2 com os valores do vetor vlin1 por ordem inversa.
16. Crie um vetor linha vlin que seja a junção dos vetores vlin1 e vlin2.
17. Verifique as dimensões dos seus vetores vlin1, vlin2 e vlin.

# Solução
"""

vcol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vcol[5])
vcol[7] = 100
print(vcol[1::2])
print(vcol[0::2])
vcolinv1 = vcol[::-1]
print(vcolinv1)
vcolinv2 = vcolinv1[2:7]
vlin1 = vcol[::2]
print(vlin1)
vlin2 = vlin1[::-1]
print(vlin2)

"""# Mais Listas"""


vlin = np.concatenate((vlin1, vlin2))
print(vlin)
print((vlin1, vlin2))

print(len(vlin1), len(vlin2), len(vlin))

lista = np.arange(4, 32, 3)
print(lista)
print(len(lista))

listamaior = np.arange(0, len(lista)*3, 1, dtype=int)
print(len(listamaior))

time = np.linspace(2, 5, num=10)
print(time)
print(len(time))

"""# Exercícios

18. Crie um vetor linha vlin100 com os números de 1 a 100.
19. Crie um vetor linha vpar100 com os números pares entre 1 e 100.
20. Crie um vetor linha vimpar100 com os números impares entre 1 e 100.
21. Crie um vetor linha vlincem com os números de vpar100 e de vimpar100 alternados. No final este vetor deverá ter os números de 1 a 100.

# Solução
"""

vlin100 = np.arange(1, 101, 1)
print(vlin100)
print(len(vlin100))

vpar100 = vlin100[1::2]
print(vpar100)
vimpar100 = vlin100[0::2]
print(vimpar100)

vlincem = np.arange(0, len(vlin100), 1, dtype=int)
print(len(vlincem))
print(vlincem)

vlincem[0::2] = vimpar100
print(vlincem)

vlincem[1::2] = vpar100
print(vlincem)

"""# Plot"""


tempo = np.arange(1/8, 2, 1/64)
sinal = 6*np.sin(2*np.pi*tempo)
plt.plot(tempo, sinal)

plt.figure(figsize=(15, 5))
plt.plot(tempo, sinal)
plt.title('Plot')
plt.ylabel('Sinal')
plt.xlabel('tempo')
plt.show()

"""# Matrizes"""

A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Dimensão de A: ', np.shape(A))  # np.shape -> Indica a forma do vetor

print('\n A = \n', A)

print('\n Linha 1 e coluna 4 de A:',  A[0, 3])

print('\n Multiplicação coeficiente a coeficiente: \n', A * A)

print('\n Multiplicação de matrizes: \n', A @ np.transpose(A))

"""# Exercícios

1. Defina uma variável A contendo matriz de 3 linhas e 4 colunas com números à
sua escolha.
2. Crie uma nova variável B contendo o valor que se encontra na linha 2 coluna 2
da sua variável A.
3. Altere o valor que se encontra na linha 3 coluna 2 da sua variável A, para 10.
4. Crie uma nova variável C contendo a segunda linha da sua variável A.
5. Crie uma nova variável D contendo a segunda coluna da sua variável A.
6. Crie uma nova variável E contendo os valores das linha 2 e 3 e das colunas 2 e 3, da sua variável A.
7. Crie uma nova variável F contendo os valores da sua variável A, mas com as linhas invertidas.
8. Crie uma nova variável G contendo os valores da sua variável A, mas com as colunas invertidas.
9. Crie uma nova variável H contendo os valores da sua matriz A que se encontram nas posições pares (linhas colunas pares).
10. Verifique as dimensões das suas matrizes A, C e D.

# Soluções
"""

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.shape(A))
print('\n A = \n', A)

B = A[1, 1]
print('\n B = ', B)

A[2, 1] = 10
print('\n A = \n', A)

C = A[1, :]
print('\n C = ', C)

D = np.transpose(A[:, 1], 0)
print('\n D = ', D)

E = A[1:3, 1:3]
print('\n E = \n', E)

F = A[::-1, :]
print('\n F = \n', F)

G = A[:, ::-1]
print('\n G = \n', G)

H = A[1::2, 1::2]
print('\n H = ', H)

print('\n Dimensão de A: ', np.shape(A))
print(' Dimensão de C: ', np.shape(C))
print(' Dimensão de D: ', np.shape(D))

"""# Mais exercícios

11. Crie um vetor linha vlin contendo todos os valores da sua variável A.
12. Crie uma nova variável I resultante da transposta da sua matriz A.Verifique as dimensões da matriz transposta.
13. Defina uma variável Z contendo uma matriz de zeros com 6 linhas e 8 colunas.
14. Copie os valores da sua matriz A para as posições pares (linhas e colunas pares)
da sua matriz Z .
15. Copie os valores da sua matriz A para as posições ímpares (linhas e colunas
ímpares) da sua matriz Z .
16. Copie os valores da sua matriz A para as posições em que as linhas são ímpares
e as colunas são pares da sua matriz Z .
17. Copie os valores da sua matriz A para as posições em que as linhas são pares e
as colunas são ímpares da sua matriz Z .

# Soluções
"""

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

"""# Mais exercícios

18. Defina uma variável rot90A contendo os valores da matriz A rodados 90◦.
19. Defina uma variável rot180A contendo os valores da matriz A rodados 180◦.
20. Defina uma variável Fim como sendo um vetor contendo em a soma dos valores de cada linha da matriz A.

# Soluções
"""

rot90A = np.transpose(A)
rot90A = rot90A[::-1, :]

print('rot90A = \n', rot90A)


def rot90(X):
    X = np.transpose(X)
    X = X[::-1, :]
    return X


def rot180(X):
    X = rot90(X)
    X = rot90(X)
    return X


print(rot90(A))

print(rot180(A))

FIM = np.sum(A, 1)
print(FIM)

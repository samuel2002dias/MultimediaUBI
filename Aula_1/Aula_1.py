import matplotlib.pyplot as plt
import numpy as np
tempo = np.arange(1/8,2,1/64)
sinal = np.sin(2*np.pi*tempo)
plt.plot(tempo,sinal)

mQ = [9/2, 9/2, -9/2, -9/2]

plt.plot (tempo[0:4], sinal[0:4], tempo[0:4], mQ)
plt.show()

Erro = ((sinal[0:4] - mQ)*(sinal[0:4] - mQ))
print("Erro de quantização: ", Erro)
ErroMedio = np.sum(Erro)/4
print ('Erro Médio: ', ErroMedio)

Codigo = np.array(['1010', '1010', '0001', '0001'])
print('Código: ', Codigo)


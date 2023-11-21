#import wave
import matplotlib.pyplot as plt
import numpy as np

from scipy.io import wavfile

# https://ipython.org/ipython-doc/stable/api/generated/IPython.display.html
# Para testar o Audio
from IPython.display import Audio, display
framerate = 44100
t = np.linspace(0,5,framerate*5)
data = np.sin(2*np.pi*220*t) + np.sin(2*np.pi*224*t)
Audio(data,rate=framerate)

""" # 1 - Ler os ficheiros de áudio 'bass.wav', 'guitar.wav', 'drums.wav'."""



sample_freq_bass, bass = wavfile.read('Audios/bass.wav')

sample_freq_guitar, guitar = wavfile.read('Audios/guitar.wav')

sample_freq_drums, drums = wavfile.read('Audios/drums.wav')




"""# 2 - Verificar a frequência de amostragem de cada um dos áudio."""

#---------------------------------------------------
#Ficha 2 - Ex 2

print('numero de amostras por segundo do bass:', sample_freq_bass)

print('numero de amostras por segundo do guitar:', sample_freq_guitar)

print('numero de amostras por segundo do drums:', sample_freq_drums)

L = bass.shape
print(L)

print(bass.size, bass.shape)

""" # 3 - Verificar a duração em segundos de cada áudio."""

n_samples_bass = bass.size
print('numero total de amostras bass:', n_samples_bass)

duration_bass = n_samples_bass/sample_freq_bass
print('duração do audio bass (segundos):', duration_bass)

n_samples_guitar = guitar.size
print('numero total de amostras guitar:', n_samples_guitar)

duration_guitar = n_samples_guitar/sample_freq_guitar
print('duração do audio guitar (segundos):', duration_guitar)

n_samples_drums = drums.size
print('numero total de amostras guitar:', n_samples_guitar)

duration_drums = n_samples_drums/sample_freq_drums
print('duração do audio drums (segundos):', duration_drums)

""" #4 - Selecionar o segundo 12 do audio drum"""
'''signal_wave_bass = bass.readframes(-1)
signal_wave_guitar = guitar.readframes(-1)
signal_wave_drums = drums.readframes(-1)'''
# Amplitude -1 


start_time_seconds = 12 
end_time_seconds = 13   


start_sample = int(start_time_seconds * sample_freq_drums)
end_sample = int(end_time_seconds * sample_freq_drums)


drums_12 = drums[start_sample:end_sample]

Audio(drums_12, rate = sample_freq_drums)


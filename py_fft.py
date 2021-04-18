from scipy.fft import fft, ifft, fftfreq
from scipy.io import wavfile
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import wave
import struct
import serial
import time

print("Hello")
N = 1000
Fs = 41466

ser = serial.Serial('/dev/ttyS3', baudrate=2000000) 
esp32_data_raw = ser.read(N * 2) # 2 bytes per sample
count = len(esp32_data_raw) // 2 # 2 bytes per sample
print(type(esp32_data_raw))

esp32_data_int = struct.unpack('<' + count * 'H', esp32_data_raw)
print(type(esp32_data_int))

# reading in wave file with scipy
# samplerate, samples = wavfile.read('CSC_sine_1000Hz.wav')
samples = np.asarray(esp32_data_int) 
# scalar = (2 ^ 5)
# samples = np.true_divide(samples, scalar)
y = samples[0:N]

print (y.size)
T = 1.0 / Fs
print("N = {}".format(N))
print("T = {}".format(T))

x = np.linspace(0.0, N*T, N, endpoint=False)
# y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

xf = fftfreq(N, T)[:N//2]
yf = fft(y)


print(yf[10])

# plot time domain

plt.plot(x, y) 
plt.show()
# time.sleep(10)



# plot frequency domain
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) 
# x_index_max = y.size / 2
# plt.xlim([0, x_index_max])


ser.close()             # close port
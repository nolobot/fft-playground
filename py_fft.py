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
N = 10000
Fs = 2777
Ts = 1.0 / Fs
print("N = {}".format(N))
print("Ts = {}".format(Ts))

ser = serial.Serial('/dev/ttyS10', baudrate=2000000) 
ser.write(b'r') # 2 bytes per sample
esp32_data_packet = ser.readline().decode("utf-8")  # 2 bytes per sample
esp32_data_raw_str = esp32_data_packet.split(',')

esp32_data_raw = [int(x) for x in esp32_data_raw_str]

# esp32_data_int_lsb = struct.unpack('<' + 'H' * count, esp32_data_raw)
# esp32_data_int_msb = struct.unpack('>' + 'H' * count, esp32_data_raw)
# esp32_data_int = struct.unpack('B' * len(esp32_data_raw), esp32_data_raw)

# reading in wave file with scipy
# samplerate, samples = wavfile.read('CSC_sine_1000Hz.wav')
# samples_lsb = np.asarray(esp32_data_int_lsb) 
# samples_msb = np.asarray(esp32_data_int_msb) 

# y_lsb = samples_lsb[0:N]
# y_msb = samples_msb[0:N]
x = np.linspace(0.0, N*Ts, N, endpoint=False)

# plot time domain
plt.plot(esp32_data_raw) 
plt.show()

# plot frequency domain
# xf = fftfreq(N, Ts)[:N//2]
# yf = fft(y)
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) 
# x_index_max = y.size / 2
# plt.xlim([0, x_index_max])

ser.close()             # close port
from scipy.fft import fft, ifft, fftfreq
from scipy.io import wavfile
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import wave
import struct
import serial
import time

Fs = 42100
Ts = 1.0 / Fs

ser = serial.Serial('/dev/ttyS10', baudrate=921600) 

plt.ion()

for x in range(0, 100):
    ser.write(b'r')
    esp32_data_packet = ser.readline().decode("utf-8")  # 2 bytes per sample
    esp32_data_raw_str = esp32_data_packet.split(',')
    
    y = [int(x) for x in esp32_data_raw_str]
    N = len(y)

    x = np.linspace(0.0, N*Ts, N, endpoint=False)

    # figure, axis = plt.subplots(2) # plot 2 plots 1 over the other

    # axis[0].clear()
    # axis[1].clear()

    # plot time domain
    # plt.plot(x, y) 

    # plot frequency domain
    xf = fftfreq(N, Ts)[:N//2]
    yf = fft(y)

    # numBins = 10
    # binSize = int(xf[-1:]) // numBins # number of indices to combine in each bin
    # numIndicesPerBin = int(len(xf) // numBins)
    # for (
    # print(numIndicesPerBin)
    # print("frequency range of each bin: {}".format(binSize))
    # binsX = np.linspace(binSize, numBins*binSize, binSize)
   

    plt.clf()
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) 
    # axis[1].set_title("Frequency Domain")
    plt.xlim([20, 20000])
    plt.pause(3)

ser.close()             # close port
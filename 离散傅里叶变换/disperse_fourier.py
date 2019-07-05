# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 9:19
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : disperse_fourier.py
# @Software: PyCharm

# 离散傅里叶变换工作

import numpy as np
import matplotlib.pyplot as plt


srate = 1000
times = np.arange(0, 2, 1/srate)
signal = 10 * np.sin(2 * np.pi * 4 * times) + 1.5 * np.sin(2 * np.pi * 6.5 * times)

pnts = len(times)
four_time = np.arange(0, pnts)/pnts
f_coefs = np.zeros(len(signal))

for i in np.arange(0, pnts-1):
    cos_wave = np.cos(2 * np.pi * i * four_time * -1)
    sin_wave = np.sin(2 * np.pi * i * four_time * -1)
    xxs = np.abs(complex(np.dot(signal, cos_wave), np.dot(signal, sin_wave))) / pnts
    f_coefs[i] = xxs * 2


print(f_coefs[0:20])
hz = np.linspace(0, srate/2, np.floor(pnts/2) + 1)
fig, ax = plt.subplots(2, 1)
ax[0].plot(times, signal)
ax[1].plot(hz[0:20], f_coefs[0:20])
plt.show()











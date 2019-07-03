# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 11:54
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : dot_product.py
# @Software: PyCharm

# 点积的基本计算

import numpy as np
import matplotlib.pyplot as plt


v1 = [1, 2, 3]
v2 = [2, 3, 4]

# 两个向量的点积
print(np.dot(v1, v2))


# 两个正弦波的点积
def sin_dot():
    x = np.linspace(0, 2, 500)

    freq1 = 5
    freq2 = 5

    ampl1 = 2
    ampl2 = 2

    theta1 = 0
    theta2 = 0

    line1 = ampl1 * np.sin(2 * np.pi * freq1 * x + theta1)
    line2 = ampl2 * np.sin(2 * np.pi * freq2 * x + theta2)
    dp = np.dot(line1, line2)
    return dp


# 一个信号和正弦波的点积
def signal_dot():
    x = np.linspace(-1, 1, 1000)
    theta = np.pi
    signal = np.sin(2 * np.pi * 5 * x + theta) * np.exp((x**2 * -1)/2)

    sin_freq = np.arange(2, 10, 0.5)
    dps = np.zeros(len(sin_freq), dtype=float)
    for i in np.arange(len(sin_freq)):
        sin_wave = np.sin(2 * np.pi * i * x)
        dps[i] = np.dot(signal, sin_wave)/len(sin_wave)

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(x, signal)
    ax[1].plot(sin_freq, dps)
    plt.show()


# print(sin_dot())
signal_dot()
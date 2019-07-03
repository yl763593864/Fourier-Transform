# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 17:06
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : complex_dot.py
# @Software: PyCharm

# 复数点积

import numpy as np
import matplotlib.pyplot as plt


# 一个信号和复数的点积
# 分别和正弦,余弦点积,然后计算他们组成的复数的幅值
def signal_dot():
    x = np.linspace(-1, 1, 1000)
    theta = 3
    signal = np.sin(2 * np.pi * 5 * x + theta) * np.exp((x**2 * -1)/2)

    sin_freq = np.arange(2, 10, 0.5)
    dps = np.zeros(len(sin_freq), dtype=float)
    angles = np.zeros(len(sin_freq))
    for i in np.arange(len(sin_freq)):
        sin_wave = np.sin(2 * np.pi * i * x)
        cos_wave = np.cos(2 * np.pi * i * x)
        dps[i] = np.abs(complex(np.dot(signal, cos_wave)/len(cos_wave),
                         np.dot(signal, sin_wave)/len(sin_wave)))
        angles[i] = np.angle(complex(np.dot(signal, cos_wave)/len(cos_wave),
                         np.dot(signal, sin_wave)/len(sin_wave)))

    fig, ax = plt.subplots(3, 1)
    ax[0].plot(x, signal)
    ax[1].plot(sin_freq, dps)
    ax[2].plot(sin_freq, angles)
    plt.show()


signal_dot()


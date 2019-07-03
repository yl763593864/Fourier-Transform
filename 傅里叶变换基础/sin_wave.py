# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 16:43
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : sin_wave.py
# @Software: PyCharm

# 正弦波和复数正弦波

import numpy as np
import matplotlib.pyplot as plt


# 显示正弦图形,a是幅度,k是频率,theta是相位
def show_sin_wave(a: float, k: float, theta: float):
    fig, ax = plt.subplots(2, 1)
    x = np.arange(0, 4, 0.01)
    y = a * np.sin(2 * np.pi * k * x + theta)
    a *= 2
    k *= 2
    theta *= 2
    # y1的正弦波幅度,频率,相位都是y的二倍
    y1 = a * np.sin(2 * np.pi * k * x + theta)
    ax[0].plot(x, y)
    ax[1].plot(x, y1)
    plt.show()


# 同时显示正弦波和余弦波
def show_sin_and_cos_wave(a: float, k: float, theta: float):
    fig, ax = plt.subplots()
    x = np.arange(0, 2, 0.01)
    cos_y = a * np.cos(2 * np.pi * k * x + theta)
    sin_y = a * np.sin(2 * np.pi * k * x + theta)
    plt.plot(x, cos_y)
    plt.plot(x, sin_y, 'r')
    plt.show()


# 显示复数正弦波
def complex_sin(a: float, k: float, theta: float):
    x = np.arange(0, 2, 0.01)
    csw = [a * np.exp(complex(0, 2 * np.pi * k * i + theta)) for i in x]

    fig, ax = plt.subplots()
    # label标签不显示
    plt.plot(x, [num.real for num in csw], )
    plt.plot(x, [num.imag for num in csw], 'r')
    # 显示标签
    plt.legend(['real', 'imag'])
    plt.show()


# show_sin_wave(1, 2, 3)
# show_sin_and_cos_wave(2, 1, 4)
complex_sin(1, 2, 3)

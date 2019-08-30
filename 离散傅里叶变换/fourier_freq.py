# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 12:30
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : fourier_freq.py
# @Software: PyCharm


'''如何将无意义的频率位置转换到有意义的单位上去
    理解(奈奎斯特频率),并能自己设置傅里叶变换的频率极限值'''

import numpy as np
import matplotlib.pyplot as plt
import math


pnts = 16
four_time = np.arange(0, pnts) / pnts

fig, ax = plt.subplots(4, 4)

for i in np.arange(16):
    real = np.cos(-1 * 2 * math.pi * i * four_time)
    imag = np.sin(-1 * 2 * math.pi * i * four_time)

    ax[i//4][int(math.fmod(i, 4))].plot(four_time, real, 'r')
    ax[i//4][int(math.fmod(i, 4))].plot(four_time, imag)


plt.show()

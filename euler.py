# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 16:38
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : euler.py
# @Software: PyCharm

# 欧拉公式
import numpy as np
import matplotlib.pyplot as plt


# 任意角度在单位圆的位置
def unit_circle(k):
    fig, ax = plt.subplots()

    # 先画一个圆
    angles = np.arange(0, 2 * np.pi, 0.01)
    x_nums = np.cos(angles)
    y_nums = np.sin(angles)
    plt.plot(x_nums, y_nums)

    plt.plot(np.cos(k), np.sin(k), 'ro')
    plt.show()


# 欧拉公式
def euler_show(m, k):
    complex_num = m * np.exp(complex(0, k))
    print(complex_num, m * np.cos(k), m * np.sin(k))
    mag = np.abs(complex_num)
    phs = np.angle(complex_num)


# unit_circle(45649)
euler_show(10, 3)
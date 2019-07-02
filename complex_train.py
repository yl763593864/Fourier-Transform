# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 16:33
# @Author  : tys
# @Email   : yangsongtang@gmail.com
# @File    : complex_train.py
# @Software: PyCharm

# 复数的一些基本信息
import numpy as np
import math
import matplotlib.pyplot as plt


# 创建一个复数
a = 4 + 3j
b = complex(4, 3)

# 打印复数的类型,实数,虚数,共轭复数
print(type(a), a.real, a.imag, a.conjugate())


# 复数的长度,先判断是否是复数,如果不是就抛出异常
def complex_length(num):
    if type(num) != complex:
        raise Exception("数据不是复数形式", num)
    else:
        return np.sqrt(num.real**2 + num.imag**2)  # 也可以使用np.abs(num)


# 复数的角度
def complex_angle(num):
    if type(num) != complex:
        raise Exception("数据不是复数形式", num)
    else:
        return math.atan2(num.imag, num.real)  # 也可以使用np.angle(num)


# 复数的显示
def complex_show(num):
    fig, ax = plt.subplots()

    plt.title('复数' + str(num), fontproperties="SimHei")
    plt.xlabel('X axis real')
    plt.ylabel('Y axis is imag')  # 设置坐标轴文字标签

    ax = plt.gca()  # get current axis 获得坐标轴对象

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')  # 将右边,上边的两条边颜色设置为空 其实就相当于抹掉这两条边

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴   指定左边的边为 y 轴

    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上

    ax.set_yticks(np.arange(-5, 5))
    ax.set_xticks([-5, -3, -3, -2, -1, 1, 2, 3, 4, 5])  # 设置坐标轴显示标记

    plt.plot(num.real, num.imag, 'ro')
    x = np.linspace(0, num.real, 100)
    y = np.linspace(0, num.imag, 100)  # 坐标轴被强制性改为在最左下角
    plt.plot(x, y)
    plt.show()


print(a, '的长度是:', complex_length(a))
print(a, '的角度是:', complex_angle(a))
complex_show(a)
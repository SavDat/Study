import numpy as np

x_array = np.array(input().split(), dtype=float)
h_array = np.array(input().split(), dtype=float)
x_target = float(input())
h_target = float(input())

a = np.polyfit(x_array, h_array, 2)  # нахождение коэфициентов для функции


def get_trend(x, a):
    y = a[0] * x**2 + a[1] * x + a[2]  # расчет высот траектории по функции параболы
    return y


h_zero = get_trend(0, a)  # высота расположения пушки
h_target_get = get_trend(x_target, a)  # расчетная высота расположения цели
delta_h = abs(h_target - h_target_get)  # расхождение высот расположения цели

print("h0 = %6.2f, %2s" % (h_zero, 'no' if delta_h > 0.5 else 'yes'))

import matplotlib.pyplot as plt
import math


#  Опишем две функции:
def f_x(x):
    x = x * math.pi/180
    y = math.exp(math.cos(x)) + math.log1p((math.sin(0.8 * x))**2 + 1) * math.cos(x)
    return y


def y_x(x):
    x = x * math.pi/180
    y = -math.log1p((math.cos(x) + math.sin(x))**2 + 1.7) + 2
    return y


#  Зададим интервал построения функции и количество точек построения.
#  Вычислим шаг:
a = -240
b = 360
n = 100
h = (b - a) / (n - 1)

#  Сформируем списки со значениями аргументов и значениями функций в них:
x_list = [a + h * i for i in range(n)]
f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]

#  Построим линии графиков функций, зададим подпись для вывода легенды:
line_f = plt.plot(x_list, f_list, label='f(x)')
line_y = plt.plot(x_list, y_list, label='y(x)')

#  Зададим стили линий:
plt.setp(line_f, color="blue", linewidth=2)
plt.setp(line_y, color="red", linewidth=2)

#  Выведем 2 оси, установим для них позицию zero:
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

#  Выведем легенду и заголовок в область построения:
plt.legend()
plt.title("Графики функций")

#  Отобразим область построения:
plt.show()

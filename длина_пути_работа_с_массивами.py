import numpy as np

# массивы длин участков и скорости автомобиля на них:
path = np.array(input().split(), dtype=int)
speed = np.array(input().split(), dtype=int)

# длина пути от А до В и выведем результат:
len_path = np.sum(path)
# print("Расстояние между пунктами А и В :", len_path)

# время прохождения автомобилем каждого участка:
time = path / speed
# print("Время на каждом участке :", np.round(time, 2))

# общее время в пути,  при выводе округлим значения:
sum_time = time.sum()
# print("Общее время в пути : ", round(sum_time, 2))

# средняя скорость автомобиля (средняя путевая скорость):
avg_speed = len_path / sum_time
# print("Средняя скорость : ", round(avg_speed, 2))

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))

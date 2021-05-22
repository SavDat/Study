s = int(input('Сумма кредита, руб.: '))
n = int(input('Срок кредита, месяцев: '))
k = int(input('процентная ставка: '))


def dif_payment(t):
    pay_d = s/n + (s - (t - 1) * (s/n)) * k / 1200
    return pay_d


def ann_payment(t):
    ka = k / 1200
    pay_a = ((ka * (1 + ka)**n) / ((1 + ka)**n - 1)) * s
    return pay_a


total_ann = 0
total_dif = 0
for t in range(1, n + 1):
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (t, dif_payment(t), ann_payment(t)))
    total_dif += dif_payment(t)
    total_ann += ann_payment(t)
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (total_dif - s, total_ann - s))

money = int(input("Введите сумму вклада: "))
deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for x in per_cent:
    deposit.append(float(per_cent[x]*money/100))
print(str('deposit=%s' %deposit))
print('максимальный deposit', + max(deposit))

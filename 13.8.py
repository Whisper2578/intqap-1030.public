def age(owners_age):
    total_price=0
    if 0 < owners_age < 18:
        print('До 18 лет билет бесплатный! ')
    elif 18 <= owners_age < 25:
        total_price += 990
        print('Стоимость билета: 990 руб. ')
    else:
        total_price += 1390
        print('Стоимость билета: 1390 руб. ')
    return total_price
total_price = 0
while True:
    try:
        ticket_counter = int(input("Введите количество билетов: "))
        if type(ticket_counter) == int:
            break
    except ValueError:
        print('Введите целое число!: ')
i = 0
while True:
    try:
        owners_age = int(input("Введите возраст:"))
        if owners_age <= 0 or owners_age > 100:
            raise ValueError()
        else:
            i += 1
            total_price += age(owners_age)
            if i == ticket_counter:
                break
        print("Билет №" + str(i))
    except ValueError:
            print('Введите целое число от 1 до 100 ')
if ticket_counter > 3:
    total_price = total_price - ((total_price / 100) * 10)
    print("Итого, с учётом 10% скидки при регистрации более 3-х человек, к оплате " + str(total_price) + " руб.")
else:
    print("Итого к оплате " + str(total_price) + " руб.")

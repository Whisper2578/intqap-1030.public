while True:
    try:
        ticket_counter = int(input('Сколько билетов хотите приобрести?: '))
        if type(ticket_counter) == int:
            break
    except ValueError:
        print('Введите целое число!: ')
for i in range(ticket_counter):
    i += 1
    while True:
        try:
            owners_age = int(input(f'Укажите возраст владельца билета №{i}? '))
            if owners_age < 18:
                print('Билет бесплатный! ')
            elif 18 <= owners_age < 25:
                total_price += 990
                print('Стоимость билета: 990 руб. ')
            else:
                total_price += 1390
                print('Стоимость билета: 1390 руб. ')
            if type(owners_age) == int:
                break
        except ValueError:
            print('Введите целое число! ')
if ticket_counter > 3:
    total_price = total_price - ((total_price / 100) * 10)
    print(f'Итого, с учётом 10% скидки при регистрации более 3-х человек, к оплате {total_price} руб. ')
else:
    print(f'Итого к оплате {total_price} руб.')
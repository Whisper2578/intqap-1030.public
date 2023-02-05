def srt_pzrk(num_list_mod):
    for i in range(len(num_list_mod)):
        for j in range(len(num_list_mod) - i - 1):
            if num_list_mod[j] > num_list_mod[j + 1]:
                num_list_mod[j], num_list_mod[j + 1] = num_list_mod[j + 1], num_list_mod[j]
    return num_list_mod

def bin_search(num_list_mod, num_user, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if num_list_mod[middle] == num_user:
        return middle
    elif num_user < num_list_mod[middle]:
        return bin_search(num_list_mod, num_user, left, middle - 1)
    else:
        return bin_search(num_list_mod, num_user, middle + 1, right)

what = True
while what:
    try:
        num_list = input("Введите натуральные числа через пробел: ").split()
        num_list_mod = [int(x) for x in num_list]
        num_list_mod = srt_pzrk(num_list_mod)
        print('Отсортировано методом пузырек: ', num_list_mod)
        num_user = input("Индекс какого числа выводим?: ")
        num_user = int(num_user)
        what = False
    except ValueError:
            print(f'Ошибка {ValueError}')
            print('Неверное значение! ')
            what = input("Повторить ввод? (y/n): ")
            if what != 'y':
                print('Выход')
                what = False
                exit(1)
            else:
                print('Внимательнее! ')
if num_user not in num_list_mod:
     print(f'Нет числа {num_user} в последовательности. {num_list_mod}')
     if num_user < min(num_list_mod):
           print(f'число {num_user} меньше минимального. {min(num_list_mod)}')
     if num_user > max(num_list_mod):
           print(f'число {num_user} больше максимального. {max(num_list_mod)}')
     exit(1)

num_index = bin_search(num_list_mod, num_user, 0, len(num_list_mod) - 1)

print("Индекс запрашиваемого числа: ", num_index)

if num_index == 0:
    print(f'число {num_user} первое значение в списке, следующее {num_list_mod[num_index + 1]}')
elif num_index == int(len(num_list_mod)-1):
    print(f'число {num_user} последнее значение в списке, предыдущее значение {num_list_mod[num_index-1]}')
else:
    print(f'предыдущее число {num_list_mod[num_index-1]}, следующее число {num_list_mod[num_index + 1]}')
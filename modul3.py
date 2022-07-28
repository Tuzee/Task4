"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
buy_list = []
your_account = 0

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'5. Ваш счет: {your_account}')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        replenishment = int(input("Введите на какую сумму поплнить счет: " ))
        your_account += replenishment
        pass
    elif choice == '2':
        replenishment = int(input("Введите сумму покупки: " ))
        if replenishment > your_account:
            print("Недостаточно средств")
        else:
            your_account -= replenishment
            buy_name = input("Введите название покупки: ")
            buy_list.append(buy_name)
        pass
    elif choice == '3':
        print(f"Ваши покупки: {buy_list}")
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
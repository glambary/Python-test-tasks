def task1():
    """1. Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000."""
    even = odd = 0
    for x in range(100, 1000+1):
        if x % 2:
            odd += x
        else:
            even += x
    print(f'Задача №1. Сумма нечётных чисел = {odd}. Сумма чётных чисел = {even}.')


def task2(date: str):
    '''
    2. Пользователь вводит дату в формате ДД.ММ.ГГГГ. Вывести первый день месяца,
    последний день месяца, сам месяц.
    '''
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

    def get_info_about_month(month: str, year: str):
        info_about_month = {
            '01': (31, 'январь'),
            '02': (
                (29 if is_leap_year(int(year)) else 28),
                'февраль'
            ),
            '03': (31, 'март'),
            '04': (30, 'апрель'),
            '05': (31, 'май'),
            '06': (30, 'июнь'),
            '07': (31, 'июль'),
            '08': (31, 'август'),
            '09': (30, 'сентябрь'),
            '10': (31, 'октябрь'),
            '11': (30, 'ноябрь'),
            '12': (31, 'декабрь'),
        }
        return info_about_month[month]

    day, month, year = date.split('.')
    last_day_month, name_month = get_info_about_month(month, year)
    print(f'Задача №2. 1 - {last_day_month} - {name_month}')


def task3(date: str):
    '''
    3. Пользователь вводит дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ. Обрежьте
    секунды. Замените час на 10.
    '''
    print(f'Задача №3. {date[:-5]}10')


def task4(date1: str, date2: str):
    '''
    4. Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Вывести разницу
    между датами в часах, днях (целых), минутах и секундах.
    '''
    # strftime() - объект дата в строку
    # strptime() - строку в объект дата
    from datetime import datetime, timedelta

    d1 = datetime.strptime(date1, '%d.%m.%Y %H:%M')
    d2 = datetime.strptime(date2, '%d.%m.%Y %H:%M')
    time_delta = abs(d2 - d1)
    print(f'Задача №4. {time_delta}')


def task5():
    """
    5. Пользователь вводит две даты в формате ДД.ММ.ГГГГ ЧЧ:ММ. Пользователь
    вводит третью дату в формате ДД.ММ.ГГГГ ЧЧ:ММ. Определить, лежит ли дата
    внутри временного интервала, образованного первыми двумя датами.
    """
    from datetime import datetime

    def is_in_date_range(date1, date2, date3) -> bool:
        d1 = datetime.strptime(date1, '%d.%m.%Y %H:%M')
        d2 = datetime.strptime(date2, '%d.%m.%Y %H:%M')
        d3 = datetime.strptime(date3, '%d.%m.%Y %H:%M')
        return d1 <= d3 <= d2

    def test_func(func):
        data = {
            1: [('11.01.2023 12:34', '10.05.2023 17:25', '11.03.2023 12:34'), True],
            2: [('11.01.2023 12:34', '10.05.2023 17:25', '11.07.2023 12:34'), False],
            3: [('11.09.2023 12:34', '10.05.2023 17:25', '11.07.2023 12:34'), False],
        }
        print('Задача №5')
        for n in data:
            test, answer = data[n]
            assert func(*test) == answer
            print(f'\ttest №{n} is OK')

    test_func(is_in_date_range)


def task6(lst: list) -> dict:
    """
    6. На входе многомерный список, каждый элемент содержит информацию о товаре,
    количестве и цене, которые были в каком-то заказе. Например: [[Товар1, 1,500],
    [Товар2, 7,1000],[Товар1, 6,900]]
    """
    # понимаю что нужно было через return сделать, но проще вывести в консоль
    from functools import reduce

    sum_order = reduce(
        (lambda x, y: x + (y[1] * y[2])),
        lst,
        0
    )

    res = {}
    for product in lst:
        key, n, price = product
        res[key] = res.get(key, 0) + price * n

    print(f'Задача №6 {res}. Общая сумма заказа = {sum_order}')
    return res


def task14(lst):
    res = sorted(lst, key=lambda x: (x[0], x[1] * x[2]))
    print(res)
    return res


def task15():


if __name__ == '__main__':
    lst = [['Товар 1', 15, 500], ['Товар 2', 7, 1000], ['Товар 1', 6, 900], ]

    task1()
    task2('02.02.2023')
    task3('ДД.ММ.ГГГГ ЧЧ:ММ')
    task4('11.05.2023 12:34', '10.01.2023 17:25')
    task5()
    task6(lst)
    task14(lst)
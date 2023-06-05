from datetime import datetime, date


class Task9:
    # 9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.
    def __init__(self, lastname: str, name: str, patronymic: str, date_of_birth: str) -> None:
        self.lastname = lastname
        self.name = name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth

    def get_full_name(self) -> str:
        # 10. Создайте метод, который выводит ФИО.
        return f'{self.lastname} {self.name} {self.patronymic}'

    def get_age(self) -> int:
        # 11. Создайте метод, который вычисляет возраст в годах.
        today = date.today()
        date_of_birth = datetime.strptime(self.date_of_birth, '%d.%m.%Y').date()
        one_or_zero = (today.month, today.day) < (date_of_birth.month, date_of_birth.day)

        return today.year - date_of_birth.year - one_or_zero


class Task12(Task9):
    # 12. Создайте класс - наследник вашего первого класса. Перекройте в нём метод,
    # вычисляющий возраст в годах на метод, который вычисляет возраст в днях.
    def get_age(self) -> int:
        today = date.today()
        date_of_birth = datetime.strptime(self.date_of_birth, '%d.%m.%Y').date()
        return (today - date_of_birth).days

    def __tag_decorator(tag='strong'):
        # 13. Создайте декоратор для метода, который выводит ФИО. Пусть новый метод
        # выводит ФИО, заключенное в теги <strong>.
        def decorator(func):
            def wrapper(*args, **kwargs):
                return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
            return wrapper
        return decorator

    @__tag_decorator()
    def get_full_name(self):
        return super().get_full_name()


KhSY = Task9('Khadkevich', 'Sergey', 'Yurievich', '03.07.1993')
task10 = KhSY.get_full_name()
task11 = KhSY.get_age()

print(f'Задача №10. {task10}')
print(f'Задача №11. {task11}')


KhSY_12 = Task12('Khadkevich', 'Sergey', 'Yurievich', '03.07.1993')
task12 = KhSY_12.get_age()
task13 = KhSY_12.get_full_name()

print(f'Задача №12. {task12}')
print(f'Задача №13. {task13}')

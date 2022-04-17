"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main(one, two):
    if type(one) == str and type(two) == str:
        if one == two:
            return 1
        elif one != two and len(one) > len(two):
            return 2
        elif one != two and two == 'learn':
            return 3
        else:
            print('Nothing')
    else:
        return 0


if __name__ == "__main__":
    print(main('ffefdkl', 'ddfcd'))
    print(main('ddfcd', 'ddfcd'))
    print(main('ddfcd', 'learn'))
    print(main('78', 'learn'))
    print(main('fdf', 'hjhnm'))

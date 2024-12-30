import sys

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    try:
      A = tuple(map(int, input("Введите 10 целых чисел через пробел: ").split()))
    except ValueError:
        print("Ошибка ввода: Введите целые числа.", file=sys.stderr)
        exit(1)

    # Проверить количество элементов кортежа.
    if len(A) != 10:
        print("Ошибка: В кортеже должно быть 10 элементов.", file=sys.stderr)
        exit(1)

    # Найти искомую сумму.
    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    # Вывести сумму
    print("Сумма элементов, модуль которых меньше 5:", s)
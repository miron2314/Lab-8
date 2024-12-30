import sys


def is_sorted_ascending(input_tuple):
    if len(input_tuple) <= 1:
        return True
    for i in range(len(input_tuple) - 1):
        if input_tuple[i] > input_tuple[i + 1]:
            return False, i + 1
    return True
if __name__ == '__main__':
    try:
        input_str = input("Введите 10 целых чисел через пробел: ")
        A = tuple(map(int, input_str.split()))
    except ValueError:
        print("Ошибка: Введены некорректные данные. Пожалуйста, введите целые числа.", file=sys.stderr)
        exit(1)

    if len(A) != 10:
        print("Ошибка: В кортеже должно быть ровно 10 элементов.", file=sys.stderr)
        exit(1)

    is_sorted, index = is_sorted_ascending(A)

    if is_sorted:
        print("Кортеж упорядочен по возрастанию.")
    else:
        print("Кортеж НЕ упорядочен по возрастанию. Первый нарушающий элемент имеет индекс:", index)
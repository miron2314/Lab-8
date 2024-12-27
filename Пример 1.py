import random

def sum_elements_less_than_5(tuple_A):
    """
    Вычисляет сумму элементов кортежа, модуль которых меньше 5.

    Args:
      tuple_A: Кортеж чисел.

    Returns:
      Сумма элементов, модуль которых меньше 5. Возвращает 0, если кортеж пуст.
    """
    if not tuple_A: # проверка на пустой кортеж
        return 0
    sum_elements = sum(x for x in tuple_A if abs(x) < 5)
    return sum_elements


#Пример использования:
# Создаем кортеж из 10 случайных чисел
tuple_A = tuple(random.randint(-10, 10) for _ in range(10))
print("Кортеж:", tuple_A)

# Вычисляем сумму элементов
sum_less_than_5 = sum_elements_less_than_5(tuple_A)
print("Сумма элементов, меньших 5 по модулю:", sum_less_than_5)


#Пример с пустым кортежем
tuple_B = ()
sum_less_than_5_B = sum_elements_less_than_5(tuple_B)
print("Сумма элементов для пустого кортежа:", sum_less_than_5_B)

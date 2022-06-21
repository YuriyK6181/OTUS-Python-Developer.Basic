"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(int_list):
    return [i ** 2 for i in int_list]

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


int_array = [1, 2, 5, 7]
print('Work with function power_numbers ========')
print("List of numbers is", list(int_array), ', square of numbers is', power_numbers(int_array))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def int_is_even(num):
    return num % 2 == 0


def int_is_odd(num):
    return num % 2 == 1


def int_is_prime(num):
    result = True

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                result = False
                break
    return result

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


def filter_numbers(int_list, get_only):
    if get_only == ODD:
        return list(filter(int_is_odd, int_list))
    elif get_only == EVEN:
        return list(filter(int_is_even, int_list))
    elif get_only == PRIME:
        return list(filter(int_is_prime, int_list))
    else:
        return None


int_array = range(20)
print('Work with function filter_numbers ========')
print('Full  list    is:', list(int_array))
print('ODD   numbers is:', filter_numbers(int_array, ODD))
print('EVEN  numbers is:', filter_numbers(int_array, EVEN))
print('PRIME numbers is:', filter_numbers(int_array, PRIME))

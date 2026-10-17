from functools import reduce


def sum_numbers(numbers):
    """Возвращает сумму чисел через reduce."""
    return reduce(lambda x, y: x + y, numbers, 0)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print("Числа:", numbers)
    print("Сумма:", sum_numbers(numbers))
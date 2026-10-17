import random


def random_numbers(start, end, count):
    """Генерирует заданное количество случайных чисел в диапазоне."""
    for _ in range(count):
        yield random.randint(start, end)


if __name__ == "__main__":
    print("Случайные числа:")

    for number in random_numbers(1, 100, 5):
        print(number)
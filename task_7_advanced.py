import random


def infinite_random_data():
    """Бесконечно генерирует случайные данные."""
    counter = 1

    while True:
        yield {
            "id": counter,
            "value": random.randint(1, 100),
        }
        counter += 1


if __name__ == "__main__":
    generator = infinite_random_data()

    print("Первые 5 случайных записей:")

    for _ in range(5):
        print(next(generator))
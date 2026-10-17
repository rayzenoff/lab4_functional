class NumberIterator:
    """Итератор чисел в заданном диапазоне."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


if __name__ == "__main__":
    numbers = NumberIterator(1, 5)

    print("Числа итератора:")

    for number in numbers:
        print(number)
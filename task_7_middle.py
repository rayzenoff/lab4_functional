from functools import wraps


def log_call(func):
    """Декоратор для логирования вызова функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")

        result = func(*args, **kwargs)

        print(f"Результат: {result}")
        return result

    return wrapper


@log_call
def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


if __name__ == "__main__":
    add(5, 7)
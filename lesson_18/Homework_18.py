# 🔁 Генератори

def even_numbers(n):
    """Генератор парних чисел від 0 до N"""
    for i in range(0, n + 1, 2):
        yield i

def fibonacci(n):
    """Генератор чисел Фібоначчі до N"""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# 🔁 Ітератори

class ReverseIterator:
    """Ітератор для зворотного обходу списку"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class EvenIterator:
    """Ітератор для парних чисел до N"""
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

# ✨ Декоратори

def log_args_result(func):
    """Декоратор для логування аргументів та результату"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик функції: {func.__name__}")
        print(f"[LOG] Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Результат: {result}")
        return result
    return wrapper

def handle_exceptions(func):
    """Декоратор для обробки винятків"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] Сталася помилка: {e}")
            return None
    return wrapper

# ✅ Тести та приклади використання

if __name__ == "__main__":
    print("== Генератор парних чисел до 10 ==")
    for num in even_numbers(10):
        print(num, end=" ")
    print("\n")

    print("== Генератор Фібоначчі до 21 ==")
    for num in fibonacci(21):
        print(num, end=" ")
    print("\n")

    print("== Зворотний ітератор списку ==")
    for item in ReverseIterator([1, 2, 3, 4]):
        print(item, end=" ")
    print("\n")

    print("== Ітератор парних чисел до 10 ==")
    for num in EvenIterator(10):
        print(num, end=" ")
    print("\n")

    @log_args_result
    def multiply(x, y):
        return x * y

    print("== Логування виклику multiply(3, 4) ==")
    multiply(3, 4)
    print()

    @handle_exceptions
    def divide(a, b):
        return a / b

    print("== Обробка винятку при divide(10, 0) ==")
    divide(10, 0)
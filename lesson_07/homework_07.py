# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break  # якщо результат більше 25 — зупинити цикл
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1  # інкрементуємо multiplier

multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def add_numbers_from_input():
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        result = a + b
        print("Сума:", result)
    except ValueError:
        print("Помилка: потрібно вводити тільки числа.")

# Виклик функції
add_numbers_from_input()


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_from_input():
    try:
        user_input = input("Введіть числа через пробіл або кому: ")
        # Розділення рядка на числа
        numbers = [float(x) for x in user_input.replace(',', ' ').split()]

        if not numbers:
            print("Список порожній. Немає що обчислювати.")
            return

        average = sum(numbers) / len(numbers)
        print("Середнє арифметичне:", average)
    except ValueError:
        print("Помилка: потрібно вводити лише числа.")


# Виклик функції
average_from_input()

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string_from_input():
    text = input("Введіть рядок: ")
    reversed_text = text[::-1]
    print("Рядок у зворотному порядку:", reversed_text)

# Виклик функції
reverse_string_from_input()

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_from_input():
    user_input = input("Введіть слова через пробіл: ")
    words = user_input.split()

    if not words:
        print("Список порожній.")
        return

    longest = max(words, key=len)
    print("Найдовше слово:", longest)


# Виклик функції
longest_word_from_input()

# task 6
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len2 == 0:
        return 0  # порожній рядок вважаємо підрядком на позиції 0

    for i in range(len1 - len2 + 1):
        if str1[i:i+len2] == str2:
            return i
    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
#apples = 2
#banana = x

def get_bananas():
    apples = int(input("Введіть кількість яблук: "))
    banana_input = int(input("Введіть кількість бананів в 4 рази більше: "))

    correct_banana = apples * 4
    if banana_input != correct_banana:
        print(f"Кількість бананів має бути в 4 рази більше за яблука ({correct_banana}). Виправляю.")
        banana_input = correct_banana

    print(f"Яблук: {apples}")
    print(f"Бананів: {banana_input}")

get_bananas()

# task 8

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
# perimetery = ? + ? + ? + ?
# print()

def calculate_perimeter():
    storona_1 = float(input("Введіть довжину сторони 1: "))
    storona_2 = float(input("Введіть довжину сторони 2: "))
    storona_3 = float(input("Введіть довжину сторони 3: "))
    storona_4 = float(input("Введіть довжину сторони 4: "))

    perimeter = storona_1 + storona_2 + storona_3 + storona_4
    print("Периметр фігури:", perimeter)

calculate_perimeter()

# task 9

#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

# Варіант 1

def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)
print(lst2)

# Варіант 2

def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]

# Отримуємо введення від користувача
user_input = input("Введіть список елементів через кому (наприклад: '1', 2, 'три', True): ")

# Перетворюємо рядок у справжній список за допомогою eval
try:
    lst = eval(f"[{user_input}]")  # обгортаємо в [] для створення списку
    lst2 = filter_strings(lst)
    print("Рядкові елементи:", lst2)
except Exception as e:
    print("Помилка обробки введених даних:", e)

# task 10

# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

def check_unique_chars():
    s = input("Введіть рядок з кілістю унікальних символів більше 10: ")
    unique_chars = set(s)
    if len(unique_chars) > 10:
        print(True)
    else:
        print(False)

check_unique_chars()


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
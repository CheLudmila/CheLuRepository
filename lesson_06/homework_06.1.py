# Отримуємо рядок від користувача
input_string = input("Введіть рядок: ")

# Підраховуємо унікальні символи
unique_characters = set(input_string)

# Перевіряємо кількість унікальних символів
if len(unique_characters) > 10:
    print(True)
else:
    print(False)
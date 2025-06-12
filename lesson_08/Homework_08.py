def sum_numbers_in_string(s):
    try:
        # Розбиваємо рядок по комі
        numbers = s.split(',')
        # Перетворюємо всі частини на int і рахуємо суму
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"

# Масив рядків
string_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Обробка кожного елемента
for item in string_list:
    result = sum_numbers_in_string(item)
    print(result)
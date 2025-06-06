lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # приклад списку з числами

# Обчислення суми парних чисел
even_sum = sum(num for num in lst if isinstance(num, int) and num % 2 == 0)

print("Сума парних чисел:", even_sum)
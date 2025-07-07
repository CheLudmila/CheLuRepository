import csv

# Заміни ці шляхи на реальні імена файлів з папки work_with_csv
file1_path = 'work_with_csv/random.csv'
file2_path = 'work_with_csv/random-michaels.csv'
output_file = 'result_Cheredniuk.csv'

# Зчитування рядків з обох файлів
rows = set()

for file_path in [file1_path, file2_path]:
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.add(tuple(row))  # Додаємо як кортеж для унікальності

# Запис результату без дублікатів у новий файл
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in sorted(rows):  # Сортування необов'язкове
        writer.writerow(row)

print(f"Готово! Результат збережено у файлі {output_file}")
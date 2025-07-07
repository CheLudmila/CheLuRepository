import os
import json
import logging

logging.basicConfig(
    filename='json__Cheredniuk.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'  # <- додано кодування
)

json_dir = 'work_with_json'

# Проходимо по кожному файлу в папці
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)  # Спроба завантажити JSON
        except json.JSONDecodeError as e:
            logging.error(f"Файл {filename} невалідний: {e}")
        except Exception as e:
            logging.error(f"Помилка при читанні файлу {filename}: {e}")

print("Перевірка завершена. Помилки (якщо були) записано в json__Cheredniuk.log.")
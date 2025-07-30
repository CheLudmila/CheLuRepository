import requests
import os

BASE_URL = 'http://127.0.0.1:8080'
IMAGE_FILE = 'example.jpg'  # тут вкажи свій файл для тесту

# 1. Завантаження зображення (POST)
with open(IMAGE_FILE, 'rb') as img:
    files = {'image': img}
    upload = requests.post(f'{BASE_URL}/upload', files=files)

if upload.status_code == 201:
    image_url = upload.json().get('image_url')
    filename = os.path.basename(image_url)  # беремо тільки назву файлу
    print(f'Завантажено: {image_url}')
else:
    print(f'Помилка завантаження: {upload.status_code} {upload.text}')
    exit()

# 2. Отримання посилання на зображення (GET)
headers = {'Content-Type': 'text'}
get_resp = requests.get(f'{BASE_URL}/image/{filename}', headers=headers)

if get_resp.status_code == 200:
    print(f"Посилання на зображення: {get_resp.json()['image_url']}")
else:
    print(f'Помилка отримання: {get_resp.status_code} {get_resp.text}')

# 3. Видалення файлу (DELETE)
delete_resp = requests.delete(f'{BASE_URL}/delete/{filename}')
if delete_resp.status_code == 200:
    print(f"Файл {filename} видалено успішно")
else:
    print(f'Помилка видалення: {delete_resp.status_code} {delete_resp.text}')
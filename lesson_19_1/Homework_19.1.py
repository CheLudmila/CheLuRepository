import requests
import os

# URL API NASA (Curiosity)
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,              # Марсіанський день
    'camera': 'fhaz',         # Камера (Front Hazard Avoidance Camera)
    'api_key': 'DEMO_KEY'     # Можна замінити на свій ключ з https://api.nasa.gov/
}

# 1. Отримуємо JSON з даними
response = requests.get(url, params=params)
if response.status_code != 200:
    print(f"Помилка запиту: {response.status_code}")
    exit()

data = response.json()
photos = data.get('photos', [])

if not photos:
    print("Фото не знайдені.")
    exit()

# 2. Створюємо папку для фото
os.makedirs('mars_photos', exist_ok=True)

# 3. Завантажуємо всі фото
for i, photo in enumerate(photos, start=1):
    img_url = photo['img_src']
    print(f"Завантаження фото {i}: {img_url}")

    try:
        img_data = requests.get(img_url, timeout=15)
        img_data.raise_for_status()
    except requests.RequestException as e:
        print(f"Не вдалося завантажити фото {i}: {e}")
        continue

    # Зберігаємо файл
    file_path = f'mars_photos/mars_photo{i}.jpg'
    with open(file_path, 'wb') as f:
        f.write(img_data.content)
    print(f"Фото збережено як {file_path}")

print(f"Завантажено {len(photos)} фото у папку mars_photos!")

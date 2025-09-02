FROM python:3.10-slim

WORKDIR /app

# встановлюємо залежності
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# копіюємо код
COPY . .

# за замовчуванням запускаємо тести з allure
CMD ["pytest", "--alluredir=allure-results"]
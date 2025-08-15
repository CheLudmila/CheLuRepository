import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

# Налаштування логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('test_search.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 🔐 Фікстура авторизації (на рівні класу)
@pytest.fixture(scope='class')
def authenticated_session():
    session = requests.Session()
    auth_url = "http://127.0.0.1:8080/auth"
    response = session.post(auth_url, auth=HTTPBasicAuth('test_user', 'test_pass'))

    assert response.status_code == 200, "Authentication failed"
    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

# 🔍 Параметризований тест пошуку автомобілів
@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        ("price", 1),
        ("year", 15),
        ("brand", 25),
    ]
)
def test_search_cars(authenticated_session, sort_by, limit):
    url = f"http://127.0.0.1:8080/cars?sort_by={sort_by}&limit={limit}"
    response = authenticated_session.get(url)

    assert response.status_code == 200, f"Failed GET /cars with sort_by={sort_by}, limit={limit}"

    cars = response.json()
    logger.info(f"GET /cars?sort_by={sort_by}&limit={limit} => returned {len(cars)} cars")
    print(f"✓ Tested sort_by={sort_by}, limit={limit}: returned {len(cars)} cars")

    # Додаткові перевірки
    assert len(cars) <= limit, "Returned more cars than limit"
    if len(cars) > 1:
        assert cars == sorted(cars, key=lambda x: x.get(sort_by)), f"Cars not sorted by {sort_by}"
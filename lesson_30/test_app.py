import pytest
import allure
from app import insert_user, update_user, delete_user, get_users

@allure.feature("CRUD Operations")
def test_crud_operations():
    with allure.step("Insert: додаємо користувача Alice"):
        insert_user("Alice", 30)
        users = get_users()
        assert len(users) == 1
        assert users[0][1] == "Alice"

    user_id = users[0][0]

    with allure.step("Update: оновлюємо ім'я та вік"):
        update_user(user_id, "Alice Smith", 31)
        users = get_users()
        assert users[0][1] == "Alice Smith"
        assert users[0][2] == 31

    with allure.step("Delete: видаляємо користувача"):
        delete_user(user_id)
        users = get_users()
        assert len(users) == 0
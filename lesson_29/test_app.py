import pytest
from app import insert_user, update_user, delete_user, get_users

def test_crud_operations():
    # Insert
    insert_user("Alice", 30)
    users = get_users()
    assert len(users) == 1
    assert users[0][1] == "Alice"

    user_id = users[0][0]

    # Update
    update_user(user_id, "Alice Smith", 31)
    users = get_users()
    assert users[0][1] == "Alice Smith"
    assert users[0][2] == 31

    # Delete
    delete_user(user_id)
    users = get_users()
    assert len(users) == 0
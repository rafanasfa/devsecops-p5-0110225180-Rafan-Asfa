users_db = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "Developer"}
]

def get_all_users():
    return users_db

def get_user_by_id(user_id):
    return next((u for u in users_db if u["id"] == user_id), None)
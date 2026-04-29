users = [
    {"name": "Alex", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Anna", "age": 30}
]
def filter_ad(users):
    return [user["name"] for user in users if user["age"] >= 18]
print(filter_ad(users))
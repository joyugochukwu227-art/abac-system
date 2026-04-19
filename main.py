from abac import check_access
from users import users
from resources import resources

tests = [
    ("Alice", "file1", "delete"),
    ("Bob", "file1", "read"),
    ("Bob", "file2", "write"),
    ("Charlie", "file2", "write"),
]

for user, resource, action in tests:
    result = check_access(users[user], resources[resource], action)

    if result:
        print(f"Access granted: {user} can {action} {resource}")
    else:
        print(f"Access denied: {user} cannot {action} {resource}")

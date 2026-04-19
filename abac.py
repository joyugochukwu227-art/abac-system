def check_access(user, resource, action):
    if user["role"] == "admin":
        return True

    if action == "read" and resource["sensitivity"] == "public":
        return True

    if action in ["write", "delete"]:
        if user["department"] == resource["department"]:
            return True

    return False

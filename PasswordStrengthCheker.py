def check_password_strength(password):
    criteria = [
        lambda p: any(x.isupper() for x in p),  # Contains at least one uppercase letter
        lambda p: any(x.islower() for x in p),  # Contains at least one lowercase letter
        lambda p: any(x.isdigit() for x in p),  # Contains at least one digit
        lambda p: any(x in "!@#$%^&*" for x in p),  # Contains at least one special character
        lambda p: len(p) >= 8  # At least 8 characters long
    ]

    messages = [
        "Password must contain at least one uppercase letter.",
        "Password must contain at least one lowercase letter.",
        "Password must contain at least one digit.",
        "Password must contain at least one special character (!@#$%^&*).",
        "Password must be at least 8 characters long."
    ]

    results = list(map(lambda criterion: criterion(password), criteria))

    if all(results):
        return "Password is strong."
    else:
        return "\n".join([messages[i] for i in range(len(criteria)) if not results[i]])

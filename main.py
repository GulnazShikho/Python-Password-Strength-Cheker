from PasswordStrengthCheker import check_password_strength


def main():
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        result = check_password_strength(password)
        print(result)
        if result == "Password is strong.":
            break


if __name__ == "__main__":
    main()

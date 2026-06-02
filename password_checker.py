def add_password():
    password = input("Enter password: ")
    return password

def check_length(password):
   return len(password)>=8


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True

    return False


def check_upper(password):
    for char in password:
        if char.isupper():
            return True

    return False


def check_lower(password):
    for char in password:
        if char.islower():
            return True

    return False


def check_special(password):
    special_chars = "!@#$%&*^"
    for char in password:
        if char in special_chars:
            return True

    return False


def password_strength(password):
    if not password:
        print("Password is not there")
        return

    score = 0

    if check_length(password):
        print("Length OK")
        score += 1
    else:
        print("Length too short")

    if check_digit(password):
        print("Contains digit")
        score += 1
    else:
        print("Missing digit")

    if check_upper(password):
        print("Contains uppercase characters")
        score+=1
    else:
        print("Uppercase missing")

    if check_lower(password):
        print("Contains lowercase characters")
        score+=1
    else:
        print("Lowercase missing")

    if check_special(password):
        print("Contains special characters")
        score+=1
    else:
        print("Special characters missing")

    print(f"Score: {score}/5\n")

    if score<=2:
        print("Weak")
    elif score<=4:
        print("Moderate")
    else:
        print("Strong")


def password_menu():
    password = ""
    while True:
        try:
            choice = int(input("Password Menu\n1-Add Password\n2-Check strength\n3-Back\n"))
        except ValueError:
            print("Non numeric value")
            continue

        match choice:
            case 1:
                password = add_password()
            case 2:
                password_strength(password)
            case 3:
                break
            case _:
                print("Wrong choice")


if __name__=="__main__":
    password_menu()
import random
import string

# Генерация email
def generate_random_email():
    generate_email = ''.join((random.choice(string.ascii_letters + string.digits) for x in range(8)))
    return f"test_{generate_email}@ya.test"


# Генерация login
def generate_random_username():
    generate_login= ''.join((random.choice(string.ascii_letters + string.digits) for x in range(6)))
    return f"test_{generate_login}"

# Генерация пароля
def generate_random_password():
    return ''.join((random.choice(string.ascii_letters + string.digits) for x in range(10)))
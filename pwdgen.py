import secrets
import string


def create_pwd(pwd_lenght=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pwd_lenght):
            pwd += ''.join(secrets.choice(alphabet))
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            pw_strong = True
    return pwd


if __name__ == '__main__':
    print(create_pwd())

# hadesthesilent#

import string


def check_pwd(pwd):
    # check for length greater than or equal 8, less than or eq to 20
    pwd_length = len(pwd)
    pwd_status = True
    if 8 <= pwd_length <= 20:
        pwd_status = True
    else:
        return False

    if any(char.islower() for char in pwd):
        pwd_status = True
    else:
        return False

    if any(char.isupper() for char in pwd):
        pwd_status = True
    else:
        return False

    if any(char.isdigit() for char in pwd):
        pwd_status = True
    else:
        return False

    return pwd_status



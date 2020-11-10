
def check_pwd(pwd):
    # check for length greater than or equal 8, less than or eq to 20
    pwd_length = len(pwd)
    if 8 <= pwd_length <= 20:
        pwd_status = True
    else:
        pwd_status = False
    return pwd_status



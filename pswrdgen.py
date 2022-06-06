import random
import string


def pswrd(letters):
    length = letters[0]
    pswrd = string.ascii_lowercase
    if letters[1] == True:
        pswrd += string.ascii_uppercase
    if letters[2] == True:
        pswrd += string.digits
    if letters[3] == True:
        pswrd += string.punctuation

    result = ''.join(random.choice(pswrd) for _ in range(length))
    return result

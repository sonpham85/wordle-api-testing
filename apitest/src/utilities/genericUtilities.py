import random
import string


def generate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return  random_string


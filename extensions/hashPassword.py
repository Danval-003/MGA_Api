import hashlib


def encoding(password):
    hash_object = hashlib.sha256()

    # Update the hash object with the password
    hash_object.update(password.encode('utf-8'))

    # Get the hashed password as a hexadecimal string
    hashed_password = hash_object.hexdigest()

    return hashed_password

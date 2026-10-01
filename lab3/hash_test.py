import hashlib


# Part 2: Hash a password using SHA-256

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# Part 2: Verify a password against a stored hash

def verify_password(password, stored_hash):

    entered_hash = hash_password(password)

    if entered_hash == stored_hash:
        return True
    else:
        return False


# Part 3: Create a simple user database

users = {
    "alice": {
        "password_hash": hash_password(
            "Cyber123!"
        )
    }
}


print(users["alice"])
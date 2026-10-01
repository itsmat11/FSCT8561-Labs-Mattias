import hashlib
import pyotp


# Part 2: Hash a password

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# Part 6: Verify a TOTP

def verify_otp(secret, otp):

    totp = pyotp.TOTP(secret)

    return totp.verify(otp)


# Part 7: Generate one secret for Alice

alice_secret = pyotp.random_base32()


# Part 7: Store password hash and TOTP secret

users = {
    "alice": {
        "password_hash": hash_password(
            "Cyber123!"
        ),
        "totp_secret": alice_secret
    }
}


print(
    "Alice's TOTP secret:",
    users["alice"]["totp_secret"]
)


# Part 8: Generate a provisioning URI

totp = pyotp.TOTP(
    users["alice"]["totp_secret"]
)

uri = totp.provisioning_uri(
    name="alice",
    issuer_name="FSCT8561-Lab3"
)

print()
print("Provisioning URI:")
print(uri)
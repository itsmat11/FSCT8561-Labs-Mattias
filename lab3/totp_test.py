import pyotp


# Part 6: Verify a TOTP value

def verify_otp(secret, otp):

    totp = pyotp.TOTP(secret)

    return totp.verify(otp)


secret = pyotp.random_base32()

totp = pyotp.TOTP(secret)

current_otp = totp.now()


print(
    "Correct OTP:",
    verify_otp(
        secret,
        current_otp
    )
)

print(
    "Wrong OTP:",
    verify_otp(
        secret,
        "000000"
    )
)
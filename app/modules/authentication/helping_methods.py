
import secrets

def generate_otp() -> str:
    return f"{secrets.randbelow(10000):04d}"
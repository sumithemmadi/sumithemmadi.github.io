import random
from Crypto.Util import number


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def modulas_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def getEncrypedMessage(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus

    return result


def generate_keypair(bits):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modulas_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key


def encrypt(message, public_key):
    n, e = public_key
    encrypted_msg = getEncrypedMessage(message, e, n)
    return encrypted_msg


def decrypt(encrypted_msg, private_key):
    n, d = private_key
    decrypted_msg = getEncrypedMessage(encrypted_msg, d, n)
    return decrypted_msg


bits = 128

while True:
    message = int(input("Enter a number: "))

    public_key, private_key = generate_keypair(bits)

    n, e = public_key
    if n <= message:
        raise Exception(
            "Generated keys are  wrong. Please try again.")

    encrypted_msg = encrypt(message, public_key)
    decrypted_msg = decrypt(encrypted_msg, private_key)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_msg}")
    print(f"Decrypted Message: {decrypted_msg}")

    break

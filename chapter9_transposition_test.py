from random import shuffle, seed, randint
from Chapter7.transportion_encryption import encrypt_message
from Chapter8.transposition_decrypt import decrypt_message
import sys


def main():
    seed(42)
    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * randint(4, 40)
        message = list(message)
        shuffle(message)
        message = "".join(message)
        print(f"Test {i + 1}: {message[:50]}")
        for key in range(1, int(len(message) / 2)):
            encrypted = encrypt_message(key, message)
            decrypted = decrypt_message(key, encrypted)

            if message != decrypted:
                print(f"Mismatch with key {key} and message {message}")
                print("Decrypted as: " + decrypted)
                sys.exit()
    print("Transposition cipher test passed.")


if __name__ == "__main__":
    main()

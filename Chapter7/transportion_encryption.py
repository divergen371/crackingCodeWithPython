import pyperclip
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="encrypt and decrypt of caesar cipher."
    )
    parser.add_argument("-m", dest="message", type=str)
    parser.add_argument("-k", dest="key", help="Amount of alphabetic shift.", type=int)

    args = parser.parse_args()
    message = args.message
    key = args.key
    cipher_text = encrypt_message(key, message)
    print(cipher_text + "|")
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_text = [""] * key

    for column in range(key):
        current_index = column

        while current_index < len(message):
            cipher_text[column] += message[current_index]
            current_index += key

    return "".join(cipher_text)


if __name__ == "__main__":
    main()

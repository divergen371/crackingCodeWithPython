from math import ceil

import pyperclip
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="decrypt of transposition cipher."
    )
    parser.add_argument("-m", dest="message", type=str)
    parser.add_argument("-k", dest="key", type=int)

    args = parser.parse_args()
    message = args.message
    key = args.key

    plaintext = decrypt_message(key, message)

    print(plaintext + "|")
    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    num_of_columns = int(ceil(len(message) / float(key)))
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    plaintext = [""] * num_of_columns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == num_of_columns) or (
            column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes
        ):
            column = 0
            row += 1
    return "".join(plaintext)


if __name__ == "__main__":
    main()

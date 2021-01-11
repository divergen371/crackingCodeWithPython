import pyperclip
import argparse
from colorama import init, Fore

init()
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
RESET = Fore.RESET


def main():
    parser = argparse.ArgumentParser(
        description="encrypt and decrypt of caesar cipher."
    )
    parser.add_argument("-m", dest="message", type=str)
    parser.add_argument("-k", dest="key", help="Amount of alphabetic shift.", type=int)
    parser.add_argument("-M", dest="mode", choices=["encrypt", "decrypt"])

    args = parser.parse_args()
    message = args.message
    key = args.key
    mode = args.mode

    caeser(key=key, message=message, mode=mode)


def caeser(key, message, mode):
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)

            if mode == "encrypt":
                translated_index = symbol_index + key
            elif mode == "decrypt":
                translated_index = symbol_index - key

            if translated_index >= len(SYMBOLS):
                translated_index = translated_index - len(SYMBOLS)
            elif translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            translated = translated + SYMBOLS[translated_index]

        else:
            translated = translated + symbol

    print(f"{BLUE}{translated}{RESET}")
    pyperclip.copy(translated)


if __name__ == "__main__":
    main()

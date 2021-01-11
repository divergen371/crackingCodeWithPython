import pyperclip
import argparse
from colorama import init, Fore

init()
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
RESET = Fore.RESET


parser = argparse.ArgumentParser(description="encrypt and decrypt of caesar cipher.")
parser.add_argument("-m", dest="message", type=str)

args = parser.parse_args()
message = args.message

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = symbol_index - key

            if translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)

            translated = translated + SYMBOLS[translated_index]
        else:
            translated = translated + symbol

    print(f"{GREEN}Key is {key}: {translated}{RESET}")

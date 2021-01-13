import os, sys, argparse
from datetime import datetime
from Chapter7.transportion_encryption import encrypt_message
from Chapter8.transposition_decrypt import decrypt_message


def main():
    parser = argparse.ArgumentParser(description="transposition cipher.")
    parser.add_argument("-i", dest="input")
    parser.add_argument("-o", dest="output")
    parser.add_argument("-k", dest="key", type=int)
    parser.add_argument("-m", dest="mode", choices=["encrypt", "decrypt"])
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    key_value = args.key
    mode = args.mode

    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist. Bye...")
        sys.exit()

    if os.path.exists(output_file):
        print(f"This will overwrite the file {output_file}.  (C)ontinue or (Q)uit?")
        res = input(">> ")
        if not res.lower().startswith("c"):
            sys.exit()

    with open(input_file, "r") as file_obj:
        content = file_obj.read()

    start_time = datetime.now()
    if mode == "enc":
        translated = encrypt_message(key_value, content)
    elif mode == "dec":
        translated = decrypt_message(key_value, content)

    total_time = datetime.now() - start_time
    print(f"Total time duration: {str(total_time)}")

    with open(output_file, "w") as output_file_obj:
        output_file_obj.write(translated)

    print(f"Finish {mode}ing {input_file} {len(content)} characters.")
    print(f"{mode}ed is {output_file}")


if __name__ == "__main__":
    main()

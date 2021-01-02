def main(msg):
    trans_result = ""
    for i in reversed(range(len(msg))):
        trans_result = trans_result + msg[i]

    return print(trans_result)


if __name__ == "__main__":
    message = input("Enter the message: ")
    main(message)

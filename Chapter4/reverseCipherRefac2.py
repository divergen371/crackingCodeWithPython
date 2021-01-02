message = input("Enter the message: ")

trans_result = ""
for i in reversed(range(len(message))):
    trans_result = trans_result + message[i]

print(trans_result)

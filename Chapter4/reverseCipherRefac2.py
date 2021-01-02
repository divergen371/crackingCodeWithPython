message = "Three can keep a secret, if two of them are dead."

trans_result = ""
for i in reversed(range(len(message))):
    trans_result = trans_result + message[i]

print(trans_result)

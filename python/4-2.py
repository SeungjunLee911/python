a = input("")

result = ""
for b in a:
    c = ord(b)
    if 65 <= c <= 90:
        result += chr(c + 32)
    elif 97 <= c <= 122:
        result += chr(c - 32)
    else:
        result += b

print(result)
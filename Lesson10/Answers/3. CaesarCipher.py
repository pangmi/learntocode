shift = int(input('Please enter any shift value: '))
message = input('Please enter any message: ')

shift %= 26
message = message.upper()

print('Actual Shift value:', shift)
print('Message:', message)

result = ''
for x in message:
    if x.isupper():
        num = ord(x)
        num += shift
        x = chr(num)
        if not x.isupper():
            num -= 26
            x = chr(num)
    
    result += x

print('Cipher Message:', result)

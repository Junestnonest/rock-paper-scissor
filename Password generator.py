import random
import string
letters= int(input("How many letter would you like in your password:"))
symbols= int(input("How many symbols would you like in your password:"))
numbers= int(input("How many numbers would you like in your password:"))
total = letters + symbols + numbers
plist = []
for i in range(letters):
    plist.append(random.choice(string.ascii_letters))
for i in range(symbols):
    plist.append(random.choice(string.punctuation))
for i in range(numbers):
    plist.append(random.choice(string.digits))
print(plist)
random.shuffle(plist)
result = ''.join(plist)
print('Your password is: {}'.format(result))

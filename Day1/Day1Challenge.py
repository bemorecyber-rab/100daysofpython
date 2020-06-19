print("Day1 Challenge - Base64")

import base64

data = open("encodedflag.txt", "r").read()

i = 0
for i in range (0,5):
    data = base64.b16decode(data)

for i in range (0,5):
    data = base64.b32decode(data)

for i in range (0,5):
    data = base64.b64decode(data)

print(data)

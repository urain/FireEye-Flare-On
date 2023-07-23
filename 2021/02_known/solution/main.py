
INT_BITS = 8
# Function to left
# rotate n by d bits
def leftRotate(n, d):
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d) | (n >> (INT_BITS - d))


# Function to right
# rotate n by d bits
def rightRotate(n, d):
    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF

import binascii
key = "No1Trust"
original = [137, 80, 78, 71, 13, 10, 26, 10] # PNG HEADER
f = open("/Users/user/Downloads/02_known/Files/critical_data.txt.encrypted","rb")
content = bytes(f.read())
cnt = 0
out = ""
for i in range(0,len(content)):
    found = 0
    for j in range(0,256): # leftover from the brute force for PNG header
        if cnt >= 8:
            cnt = 0
        keyByte = ord(key[i%8])
        encoded = (content[i] ^ keyByte) & 0xff
        encoded = leftRotate(encoded, cnt) & 0xff
        encoded = (encoded - cnt) & 0xff
        out += "%02x"%encoded
        break

        if encoded == original[i]:
            out += chr(j)
            break
        continue
    cnt += 1
    continue

f = open("out.txt","wb")
f.write(binascii.unhexlify(out))
f.close()
print(key)



import sys
encode = list("ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/")
compare = "x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q" # 52 chars / 3 = 17 chunks
password = "abcdefghijklmno"
pass_encoded= "VTGgWDSjW2emzjqpyT5s"



result = ""

#encode
for i in range(0,len(password),3):
	
	hexChunk = ord(password[i+0]) << 0x10
	hexChunk = hexChunk + (ord(password[i+1]) << 0x08)
	hexChunk = hexChunk + ord(password[i+2])

	print("%08x" % hexChunk)

	first = hexChunk >> 0x12
	first = first & 0x3f
	result = result + encode[first]
	

	second = hexChunk >> 0x0C
	second = second & 0x3f
	result = result + encode[second]


	third = hexChunk >> 0x6
	third = third & 0x3f
	result = result + encode[third]




	fourth = hexChunk >> 0x0
	fourth = hexChunk & 0x3f
	result = result + encode[fourth]
print("RESULT: %s" % result)


result = ""
for i in range(0,len(compare),4):
	
	hexChunk = 0

	#ord of letters
	first  = encode.index(compare[i+0])
	second = encode.index(compare[i+1])
	third  = encode.index(compare[i+2])
	fourth = encode.index(compare[i+3])

	firstR = first & 0x3f
	firstR = firstR << 0x12

	secondR = second & 0x3f
	secondR = secondR << 0x0c

	thirdR = third & 0x3f
	thirdR = thirdR << 0x6

	fourthR = fourth & 0x3f
	fourthR = fourthR << 0x0


	hexChunk = firstR + secondR + thirdR + fourthR

	hexStr = hex(hexChunk)[2:]
	print(hexStr)

	result = result + chr(int(hexStr[0:2],16))
	result = result + chr(int(hexStr[2:4],16))
	result = result + chr(int(hexStr[4:6],16))
	#print(int(hexStr[6:8]))

		#print(chr(int(hexStr[x:x+2])))
		#print(hexStr[x:x+2])
		#result += chr(int(hexStr[x:x+2]))

print("RESULT: %s" % result)
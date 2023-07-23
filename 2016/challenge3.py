# the exe name is hinted at by the string C:\extraspecial.pdb
# basically this will take the filename and arg after it and hash an already hashed key at 0x004181c0
# all you need to do is input 26 character arg after the filename to get the correct "hashed-hashed" key
# I realized it is the correct one by the last 32 bit hash which should be an "m" from ".com"

hashed_key =  "2F3E61EE45EB79DE3D2F1BAFD7BB47879CC49A73AEF5A4C9C1C53246249B02A0595016D65194B7A6BA239DE7CE92AE8A181A99859958E0FE94790C436FF3B91A8124C470CF27BD056F6EFFC47C84775AB37792DDFF3C842544A9DC5F9628E48EC761E92ADA3177A7"
hashed_list = []
#change endianess of the 32 bit hash chunks above
for i in range(0,len(hashed_key),8):
	temp = hashed_key[i+6:i+8]
	temp += hashed_key[i+4:i+6]
	temp += hashed_key[i+2:i+4]
	temp += hashed_key[i:i+2]
	hashed_list.append(int(temp,16))
for x in hashed_list:
	print "%08x" % x
	

result = ""
flare = "\x46\x4c\x41\x52\x45\x20\x4f\x6e\x21"
for j in range(1,0x1b):
	for h in range(0x0,0xff):
		temp = chr(h) + chr(j+0x5f) + flare
		#temp = chr(h) + flare
		cumulative = 0
		current = 0
		#print temp,
		for i in temp:
			#print "%08x\t%08x" % (cumulative,current)
			current = (cumulative * 0x24) & 0xffffffff
			#print "%08x\t%08x" % (cumulative,current)
			current = (cumulative + current) & 0xffffffff
			#print "%08x\t%08x" % (cumulative,current)
			current = (current + ord(i)) & 0xffffffff
			#print "%08x\t%08x" % (cumulative,current)
			cumulative = current & 0xffffffff
			#print "%08x\t%08x" % (cumulative,current)
			#print "------------------------\n"


		if cumulative == hashed_list[j-1]:
			result += chr(h)
			print "\nLETTER FOUND: %c" % h
			
			
		#print "\t%08x" % (cumulative)
print result

PASSWORD IS Ohs0pec1alpwd@flare-on.com



	
# # For filename
# temp = "aspecial.exe"
# cumulative = 0
# current = 0
# print temp,
# for i in temp:
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (cumulative * 0x24) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (cumulative + current) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (current + ord(i)) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# cumulative = current & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# #print "------------------------\n"
# print "\t%08x" % cumulative # result in 18fd4c


# # For arg
# temp = "a"
# cumulative = 0
# current = 0
# print temp,
# for i in temp:
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (cumulative * 0x24) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (cumulative + current) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# current = (current + ord(i)) & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# cumulative = current & 0xffffffff
	# #print "%08x\t%08x" % (cumulative,current)
	# #print "------------------------\n"
# print "\t%08x" % cumulative # result in 18fd04


#18fd4c = e71b5cc5 	after doing stuff with filename
# 18fd04 = b763cd67 after doing stuff with the argument


#fname e61b5cc5
# 004181c0	seems to hold the dword where final dword will be compared to - set bp here on write
#potential change at 401305 xoring
		
#should end with 3b687c31 for a
#print hex(cumulative)

#4181c0 seems to be the calculated byte block from filename and arg and later compared with arg hash blocks
# data here is 67 long iter'd in func 40124b
#may be changing the initial filename and arg put together routine at 401305       stack 18fd50 may change
#18 F9 27 22 A3 DD 88 AE 84 4D C8 19 6B 88 D6 C4 CD 94 94 70 F9 B2 EB 85 9D 0D 46 6F F5 2F CF B9
#16 70 05 7A 61 EA 84 1D 96 C3 57 2D 17 BD CA 74 70 C9 EE 93 A9 9F AA E3 1A A6 83 C8 A8 E4 63 29
#58 87 2D C6 1F 88 8E AC 00 61 B2 F8 0D 13 FC 72 DD 19 6E 0C 6B 2B C0 9E BB B4 B5 E1 35 3F 45 5E
#2B 28 46 0C BB ED 64 9B




#8F 48 E6 8E 
#19 37 8A EE 
#EA B1 2C 5B E5 A4 80 3D 4D 3A 93 6D 99 F6 42 F0 4F 3A 4C 92 DE 8B 19 3F
#F8 70 58 EA 29 BE 6F A9 D3 61 F4 21 A4 C8 3B 93 20 BC E0 2B C2 18 E5 8D 9B DA F3 0A BB 2E 42 14
#38 BB 5E B5 A7 7C 6B A9 34 9D 77 B3 A1 ED 5F 40 AF 16 74 F1 36 D2 72 42 DB 1A 0C D9 B9 77 0B 7D
#E4 3A AF E4 6B 31 2D 3A


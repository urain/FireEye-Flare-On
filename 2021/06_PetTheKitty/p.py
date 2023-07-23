import os
import re

f = open("stream_2","rb")
content = f.read()
f.close()

content2 = re.sub(r"ME0W.{8}PA30","FUCKFUCKFUCKPA30",content).split("FUCKFUCKFUCK")

count = 0
for i in content2:
	if len(i)>0:
		f = open("patches/%d.pa30"%count,"wb")
		f.write(i)
		f.close()
		count += 1


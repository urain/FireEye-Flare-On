import hashlib
import binascii
import random

"""
Bunch of aquatic things. Click on them and they populate two strings.
Each acquatic is assigned the following:
    sword           derelict:MZZWP
    catfish         lagan:BAJkR
    jelly           flotsam:DFWEyEW
    mermaid         flotsam:PXopvM
    nessy           derelict:LDNCVYU
    shark           derelict:yXQsGB
    stripe          jetsam:newaui
    clam            lagan:QICMX
    dolphin         lagan:rOPFG
    crab            jetsam:HwdwAZ
    seagul          jetsam:SLdkv
    seal            derelict:LSZvYSFHW
    goldfish        flotsam:BGgsuhn
    sandpiper       derelict:LSZvYSFHW
    coral           derelict:RTYXAc
    whale           lagan:GTXI
Only clicking flotsam and jetsam items actually add anything to the two strings.
After you have at least 0x1f length in each string it goes through and
does a simple xor sub routine iterating one char from each string at a 
time. It then takes the result and MD5 hashes it. Need to match the hash
against a known one in the binary.

"""

firstOptions = {"jelly":"DFWEyEW",
                "mermaid":"PXopvM",
                "goldfish":"BGgsuhn"}
firstOptionsKeys = list(firstOptions.keys())
secondOptions = {"stripe":"newaui",
                 "crab":"HwdwAZ",
                 "seagul":"SLdkv"}
secondOptionsKeys = list(secondOptions.keys())

byteThingy = b"\x96\x25\xA4\xA9\xA3\x96\x9A\x90\x9F\xAF\xE5\x38\xF9\x81\x9E\x16\xF9\xCB\xE4\xA4\x87\x8F\x8F\xBA\xD2\x9D\xA7\xD1\xFC\xA3\xA8"
targetHash = "6c5215b12a10e936f8de1e42083ba184"


while(1):
    randomFirst = ""
    randomFirstCombo = []
    randomSecond = ""
    randomSecondCombo = []

    while(len(randomFirst)<0x1f):
        firstKey = random.choice(firstOptionsKeys)
        randomFirstCombo.append(firstKey)
        randomFirst += firstOptions[firstKey]
    while(len(randomSecond)<0x1f):
        secondKey = random.choice(secondOptionsKeys)
        randomSecondCombo.append(secondKey)
        randomSecond += secondOptions[secondKey]

    hexStr = bytearray()
    for i in range(0,0x1f):
        op1 = (ord(randomFirst[i])^byteThingy[i]) & 0xff
        op2 = (op1 - ord(randomSecond[i])) & 0xff
        hexStr.append(op2)

    outHash = hashlib.md5(hexStr).hexdigest()

    if outHash == targetHash:
        print(randomFirst)
        print(randomFirstCombo)
        print(randomSecond)
        print(randomSecondCombo)
        print(binascii.hexlify(hexStr))
        break

"""
mov al, first[counter]
xor byteThingy[edi], first[counter]
mov eax, 0xf0f0f01
div stuff...dunno result was zero into eax
shr counter, 4
mov ecx, counter
shr ecx, 4

"""


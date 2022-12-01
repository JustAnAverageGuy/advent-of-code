hextobin = {hex(i)[2:].upper(): (4-len(bin(i)[2:]))
            * '0'+bin(i)[2:] for i in range(16)}

with open("testinput.txt", 'r') as file:
    bits = ''.join(map(lambda x: hextobin[x], file.readline()))


version = int(bits[:3], 2)
typeID = int(bits[3:6], 2)


def decod(bits):
    version = int(bits[:3], 2)
    typeID = int(bits[3:6], 2)
    if typeID == 4:
        ansbits = ''
        i = 6
        while int(bits[i]):
            ansbits += bits[i+1:i+5]
            i += 5
        ansbits += bits[i+1: i+5]
        return (version, int(ansbits, 2))
    else:
        if int(bits[6]):  # LengthTypeID
            numberofsubpackets = int(bits[7:18], 2)
        else:
            lengthofsubpackets = int(bits[7:22], 2)


print(bits, decod("0101001000100100"))

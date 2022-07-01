def bin8(n):    #converts an integer to an 8-bit binary number

    binary=bin(n)[2:]                      #Since bin() prefixes "0b", so we remove it by slicing it out.     
    binary=("0"*(8-len(binary)))+binary    #If the binary part in previous step is not 8-bit , then we have to add extra zeroes in the front.
    return binary[0:8]                     #We need to ensure that the no. returned is 8-bit only. So this statement deals with the case when the binary equivalent of integer 'n' is greater than 255, i.e. takes more than 8 bits to be represented. 


def bin16(n):    #converts an integer to an 16-bit binary number

    binary=bin(n)[2:]                      #Since bin() prefixes "0b", so we remove it by slicing it out.     
    binary=("0"*(16-len(binary)))+binary    #If the binary part in previous step is not 16-bit , then we have to add extra zeroes in the front.
    return binary[0:16]                     #We need to ensure that the no. returned is 16-bit only. So this statement deals with the case when the binary equivalent of integer 'n' is greater than 65535, i.e. takes more than 16 bits to be represented.



"""Same type of instructions are grouped together
under one common function. This was done since they share the same encoding style"""

def TypeA(L):
    if L[0]=="add":
        s="10000"
        
    elif L[0]=="sub":
        s="10001"
        
    elif L[0]=="mul":
        s="10110"

    elif L[0]=="xor":
        s="11010"

    elif L[0]=="or":
        s="11011"
        
    else:
        s="11100:
        
    s+="0"*2+reg[L[1]][0]+reg[L[2]][0]+reg[L[3]][0]
    return s


def TypeB(L):
    if L[0]=="mov":
        s="10010"

    elif L[0]=="rs":
        s="11000"

    else:
        s="11001"

    s+=reg[L[1]][0]+bin8(int(L[2][1:]))
    return s


def TypeC(L):
    if L[0]=="mov":
        s="10011"

    elif L[0]=="div":
        s="10111"

    elif L[0]=="not":
        s="11101"

    else:
        s="11110"

    s+="0"*5+reg[L[1]][0]+reg[L[2]][0]
    return s


def TypeD(L):
    if L[0]=="ld":
        s="10100"
        
    else:
        s="10101"

    s+=reg[L[1]][0]+L[2]
    return s


def TypeE(L):
    if L[0]=="jmp":
        s="11111"
        
    elif L[0]=="jlt":
        s="01100"

    elif L[0]=="jgt":
        s="01101"

    else:
        s="01111"

    s+="0"*3+L[1]
    return s

def TypeF(L):
    s="01010"+"0"*11
    return s

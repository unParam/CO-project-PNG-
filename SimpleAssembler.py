from sys import stdin

def binarytodecimal(str1):
    lenstr1=len(str1)
    decimal=0
    count=0
    while lenstr1>0:
        decimal+=(2**(lenstr1-1)*(int(str1[count])))
        lenstr1-=1
        count+=1
    return decimal

def decimaltobinary(str1):
    num1=int(str1)
    str2=''
    quotient=1
    while quotient!=0:
        quotient=num1//2
        remainder=num1%2
        str2+=str(remainder)
        num1=quotient
    str3=str2[::-1]
    return str3

def convert_afterdec(n):
    rem=1
    ans=0
    ans_str=''
    while(rem!=0):
        n=n*2
        if(n==1):
            ans_str+='1'
            break
        elif(n>1):
            ans_str+='1'
            ans=n-1
        elif(n<1):
            ans_str=ans_str+'0'
            ans=n
        n=ans
    return ans_str

def listToString(s):
    str1 = "" 
    for i in s:
        str1 =str1+i+" "  
    return str1

def space_error(line):
    words=len(line.split())
    spaces=0
    for i in line:
        if i==" ":
            spaces+=1
    if spaces!=words-1:
        print("Invalid spaces in line ",list_of_instructions.index(line.split()))
        exit(0)

def var_after_instruction():
    i=0
    while(list_of_instructions[i]=="" or list_of_instructions[i][0]=="var"):
        i=i+1
    for j in range(i+1,len(list_of_instructions)):
        if(list_of_instructions[j]!="" and list_of_instructions[j][0]=="var"):
            print("Variable declaration after an instruction at line ",j)
            exit(0)
        
def hlt_error():
    c=0
    for i in list_of_instructions:
        if(i==''):
            continue
        if i[0]=="hlt":
            c+=1
    if c>1:
        print("More than one hlt statements")
        exit(0)
    if list_of_instructions[-1][-1]!="hlt":
        print("Last statement is not hlt")
        exit(0)

def check_error():
    x = None
    for i in list_of_instructions:
        if(i==''):
            continue
        x = error(i)
        if (x == None):
            continue
        else:
            exit(0)
            return

def error(l):

    if (l[0] != "var" and l[0] not in all):
        print("Invalid operation in line ",list_of_instructions.index(l))
        return True
    
    elif (l[0]=="var" and ((l[1] in all))): #or (l[1][0] in ['0','1','2','3','4','5','6','7','8','9']))):
        print("Invalid variable name at line ",list_of_instructions.index(l))
        return True
    
    elif ((l[0]== 'jmp' or l[0] == 'jlt' or l[0] == 'jgt' or l[0] == 'je') and (l[1] in list(memory_address_data.keys()) or (l[1] in reg.keys() and l[0][1] !="FLAGS"))):
        print("Invalid memory address at line",list_of_instructions.index(l))
        return True
    
    # to check errors in A type instructions
    elif (l[0] == "add" or l[0] == "sub" or l[0] == "mul" or l[0] == "xor" or l[0] == "or" or l[0] == "and"):
        if (len(l) != 4):
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True
        if(l[1]=="FLAGS" or l[2]=="FLAGS" or l[3]=="FLAGS"):
            print("Invalid use of flags register at line ",list_of_instructions.index(l))
            return True
        elif (l[1] not in list(reg.keys()) or l[2] not in list(reg.keys()) or l[3] not in list(reg.keys())):
            print("Invalid register name in line ",list_of_instructions.index(l))
            return True

    # to check errors in both mov type instructions
    elif(l[0]=="mov"):
        if len(l)!=3:
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True

        elif (l[1] == "FLAGS"):
            print("Invalid use of flags register at line ",list_of_instructions.index(l))
            return True
        elif(l[2][1]=="R"):
            if(l[2] not in list(reg.keys())):
                print("Invalid register name in line ",list_of_instructions.index(l))
                return True
        elif(l[2][1]=="$"):
            if (int(l[2][1:],10)<0 and int(l[2][1:],10)>255):
                print("Invalid immidiete in line ",list_of_instructions.index(l))
                return True
    
    # to check errors in B type instructions
    elif ( l[0] == "rs" or l[0] == "ls"):
        if (len(l) != 3):
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True
        if (l[1] == "FLAGS" or l[2]=="FLAGS"):
            print("Invalid use of flags register in line ",list_of_instructions.index(l))
            return True
        elif (l[1] not in list(reg.keys())):
            print("Invalid register name in line ",list_of_instructions.index(l))  #line number
            return True
        elif(l[2][1]=="$"):
            if (int(l[2][1:],10)<0 and int(l[2][1:],10)>255):
                print("Invalid immidiete in line ",list_of_instructions.index(l))
                return True

    # to check errors in C type instructions
    elif (l[0]== "div" or l[0] == "not" or l[0] == "cmp"):
        if (len(l) != 3):
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True
        if(l[1]=="FLAGS" or l[2]=="FLAGS"):
            print("Invalid use of flags register in line ",list_of_instructions.index(l))
            return True
        elif (l[1] not in list(reg.keys()) or l[2] not in list(reg.keys())):
            print("Invalid register name in line ",list_of_instructions.index(l))
            return True

    # to check errors in D type instructions
    elif (l[0] == "ld" or l[0] == "st"):
        if (len(l) != 3):
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True
        elif(l[1]=="FLAGS"):
            print("Illegal use of flags register in line ",list_of_instructions.index(l))
            return True
        elif (l[1] not in list(reg.keys())):
            print("Invalid register name in line ",list_of_instructions.index(l))
            return True
        elif l[1] in list(labels.keys()):
            print("Use of labels instead of variable in line ",list_of_instructions.index(l))
            return True
        elif l[2] not in list(memory_address_data.keys()):
            print("Invalid memory address in line ",list_of_instructions.index(l))
            return True
    
    # to check errors in E type instructions
    elif (l[0] == "jmp" or l[0] == "jlt" or l[0] == "jgt" or l[0] == "je"):
        if (len(l) != 2):
            print("More or less arguments passed in line ",list_of_instructions.index(l))
            return True
        if l[1] in list(memory_address_data.keys()):
            print("Use of variable instead of label in line ",list_of_instructions.index(l))
            return True
        elif l[1] not in list(labels.keys()):
            print("Invalid  memory address in line ",list_of_instructions.index(l))
            return True
    
    # to check errors in F type instructions
    elif (l[0] == "hlt"):
        if (len(l) != 1):
            print("hlt instruction does bot have any arguments ",list_of_instructions.index(l))
            return True



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
    s=''
    if L[0]=="add":
        s="10000"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1+reg2
    #     # if len(str(decitobase(reg3,2)))>max(len(str(decitobase(reg2,2)))),len(str(decitobase(reg1,2))):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3
  
    elif L[0]=="sub":
        s="10001"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1-reg2
    #     # if len(str(decitobase(reg3,2)))>max(len(str(decitobase(reg2,2)))),len(str(decitobase(reg1,2))):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3
        
    elif L[0]=="mul":
        s="10110"
    #     reg1=int(reg[L[1]][1])
    #     reg2=int(reg[L[2]][1])
    #     reg3=int(reg[L[3]][1])
    #     reg3=reg1*reg2
    #     # if len(reg3)>len(reg2)+len(reg1):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3

    elif L[0]=="xor":
        s="11010"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1^reg2
    #     reg[L[3]][1]=reg3

    elif L[0]=="or":
        s="11011"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=int(reg1 or reg2)
    #     reg[L[3]][1]=reg3
        
    elif L[0]=="and":   
        s="11100"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=int(reg1 and reg2)
    #     reg[L[3]][1]=reg3

    try: 
        s+="0"*2+reg[L[1]][0]+reg[L[2]][0]+reg[L[3]][0]
        return s
    except KeyError:
        print("Invalid syntax, undefined registers being used in line",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)

def TypeB(L):
    if L[0]=="mov":
        s="10010"
        #reg[L[1]][1]=L[2][1:]

    elif L[0]=="rs":
        s="11000"
        # imm_in_binary=str(bin8(int(L[2][1:])))
        # imm_in_decimal=bin(imm_in_binary)[2:]
        # imm_in_binary=int(imm_in_binary)
        # reg1=reg[L[1]][1]
        # reg1=imm_in_binary
        # reg[L[1]][1]=reg1

    elif L[0]=="ls":
        s="11001"
        # imm_in_binary=str(bin8(int(L[2][1:])))
        # imm_in_decimal=bin(imm_in_binary)[2:]
        # imm_in_binary=int(imm_in_binary)
        # reg1=reg[L[1]][1]
        # reg1=imm_in_binary
        # reg[L[1]][1]=reg1
    
    num=int(L[2][1:])
    if(num>255 or num<0):
        print("Invalid value of immediate in line",list_of_instructions.index(L))
        exit(0)
    try:  
        s+=reg[L[1]][0]+bin8(int(L[2][1:]))
        return s
    except KeyError:
        print("Invalid syntax, undefined registers being used in line ",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)

def TypeC(L):
    
    if L[0]=="mov":
        s="10011"
        # reg1=reg[L[1]][1]
        # reg2=reg[L[2]][1]
        # reg2=reg1
        # reg[L[2]][1]=reg2

    elif L[0]=="div":
        s="10111"
        # reg1=reg[L[1]][1]
        # reg0=reg[L[0]][1]
        # reg3=reg[L[3]][1]
        # reg4=reg[L[4]][1]
        # reg0=reg3//reg4
        # reg1=reg3%reg4
        # reg[L[0]][1]=reg0
        # reg[L[1]][1]=reg1

    elif L[0]=="not":
        s="11101"
        # reg1=reg[L[1]][1]
        # reg2=reg[L[2]][1]
        # reg2=~reg1
        # reg[L[2]][1]=reg2

    elif L[0]=="cmp":        
        s="11110"
        # reg1=reg[L[1]][1]
        # reg2=reg[L[2]][1]
        # if(reg1>reg2):
        #     reg['flags'][1][-2]=1
        # elif(reg1<reg2):
        #     reg['flags'][1][-3]=1
        # elif(reg1==reg2):
        #     reg['flags'][1][-1]=1
        
    try:
        s+="0"*5+reg[L[1]][0]+reg[L[2]][0]
        return s
    except KeyError:
        print("Invalid syntax, undefined registers being used in line",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)

def TypeD(L):
    if L[0]=="ld":
        s="10100" 
        # reg1=reg[L[1]][1]
        # val=memory_address_data[L[2]]
        # reg1=val
        # reg[L[1]][1]=reg1
        
    elif L[0]=="st":
        s="10101"
        # reg1=reg[L[1]][1]
        # memory_address_data[L[2]]=reg1
        # reg[L[1]][1]=reg1

    #address=memory_address_data[L[2]]
    # if(address==''):
    #     print("Invalid syntax at line",line_number+line_adjustment-1)
    #     exit(0)
    try: 
        address=memory_address_data[L[2]]
        s+=reg[L[1]][0]+address
        return s
    except KeyError:
        print("Invalid syntax, undefined variable or register being used in line",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)



def TypeE(L):  

    if L[0]=="jmp":
        s="11111"
                
    elif L[0]=="jlt":
        s="01100"

    elif L[0]=="jgt":
        s="01101"

    elif L[0]=="je":
        s="01111"

    try:
        address=labels[L[1]]
        # if(address==''):
        #     print("Invalid syntax at line",line_number+line_adjustment-1)
        #     exit(0)

        s+="0"*3+address
        return s
    except KeyError:
        print("Invalid syntax, undefined labels being used in line",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)

def TypeF(L):  #this is halt(hlt)
    
    s="01010"+"0"*11
    return s

def TypeG(L):
    s=''
    if L[0]=="addf":
        s="00000"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1+reg2
    #     # if len(str(decitobase(reg3,2)))>max(len(str(decitobase(reg2,2)))),len(str(decitobase(reg1,2))):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3
  
    elif L[0]=="subf":
        s="00001"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1-reg2
    #     # if len(str(decitobase(reg3,2)))>max(len(str(decitobase(reg2,2)))),len(str(decitobase(reg1,2))):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3
        
    '''elif L[0]=="mul":
        s="10110"
    #     reg1=int(reg[L[1]][1])
    #     reg2=int(reg[L[2]][1])
    #     reg3=int(reg[L[3]][1])
    #     reg3=reg1*reg2
    #     # if len(reg3)>len(reg2)+len(reg1):
    #     #     reg['flags'][1][-4]=1
    #     if len(bin(reg3)[2:])>3:
    #         reg['flags'][1][-4]=1
    #     reg[L[3]][1]=reg3

    elif L[0]=="xor":
        s="11010"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=reg1^reg2
    #     reg[L[3]][1]=reg3

    elif L[0]=="or":
        s="11011"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=int(reg1 or reg2)
    #     reg[L[3]][1]=reg3
        
    elif L[0]=="and":   
        s="11100"
    #     reg1=reg[L[1]][1]
    #     reg2=reg[L[2]][1]
    #     reg3=reg[L[3]][1]
    #     reg3=int(reg1 and reg2)
    #     reg[L[3]][1]=reg3'''

    try: 
        s+="0"*2+reg[L[1]][0]+reg[L[2]][0]+reg[L[3]][0]
        return s
    except KeyError:
        print("Invalid syntax, undefined registers being used in line",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)

def TypeH(L):
    if L[0]=="movf":
        s="00010"
        #reg[L[1]][1]=L[2][1:]

    '''elif L[0]=="rs":
        s="11000"
        # imm_in_binary=str(bin8(int(L[2][1:])))
        # imm_in_decimal=bin(imm_in_binary)[2:]
        # imm_in_binary=int(imm_in_binary)
        # reg1=reg[L[1]][1]
        # reg1=imm_in_binary
        # reg[L[1]][1]=reg1

    elif L[0]=="ls":
        s="11001"
        # imm_in_binary=str(bin8(int(L[2][1:])))
        # imm_in_decimal=bin(imm_in_binary)[2:]
        # imm_in_binary=int(imm_in_binary)
        # reg1=reg[L[1]][1]
        # reg1=imm_in_binary
        # reg[L[1]][1]=reg1'''
    
    #num=float(L[2][1:])
    num=float(L[2])
    if(num>252 or num<0):
        print("Invalid value of immediate in line",list_of_instructions.index(L))
        exit(0)
    try:  
        sum_left_dec, sum_right_dec = str(num).split(".")
        #len_rt=len(sum_right_dec)
        sum_left_dec=decimaltobinary(sum_left_dec)
        #print("sum left",sum_left_dec)
        if(sum_right_dec!='0'):
            sum_right_dec='0.'+sum_right_dec
            sum_right_dec=float(sum_right_dec)
            
            sum_right_dec=convert_afterdec(sum_right_dec)
        #print("sum right",sum_right_dec)
            len_rt=len(sum_right_dec)

        else:
            len_rt=1
        

        sum_bin=sum_left_dec+'.'+sum_right_dec
        sum_bin=float(sum_bin)
        
        
        exp=0

        mantissa=len(sum_left_dec)-1
        sum_bin=sum_bin*(10**(-mantissa))
        exp=mantissa

        '''if(len_rt+mantissa>5):
            print("error more than 5 mantissa bits")
            exit(0)'''

        str1=str(sum_bin)
        str1=str1[2:]
        while(len(str1)!=5):
            str1=str1+'0'
            #reg[]
        if(exp>7 or exp<0):
            print("invalid exponent")
            exit(0)


        str2=decimaltobinary(exp)
        while(len(str2)!=3):
            str2='0'+str2
        str3=str2+str1



        #s+=reg[L[1]][0]+bin8(int(L[2][1:]))
        s+=reg[L[1]][0]+str3
        return s
        
    except KeyError:
        print("Invalid syntax, undefined registers being used in line ",list_of_instructions.index(L))
        exit(0)
    except IndexError:
        print("Invalid syntax, less arguments passed in line",list_of_instructions.index(L))
        exit(0)


reg = {'R0': ['000', 0],
       'R1': ['001', 0],
       'R2': ['010', 0],
       'R3': ['011', 0],
       'R4': ['100', 0],
       'R5': ['101', 0],
       'R6': ['110', 0],
       'FLAGS': ['111', [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]}
       

type_A=["add","sub","mul","xor","or","and"]
type_B=["mov","rs","ls"]
type_C=["mov","div","not","cmp"]
type_D=["ld","st"]
type_E=["jmp","jgt","jlt","je"]
type_F=["hlt"]
type_G=["addf","subf"]
type_H=["movf"]

all= type_A+type_B+type_C+type_D+type_E+type_F+type_G+type_H


memory_address_data={}
labels={}
list_of_instructions=[]
output_list=[]
line_number=0
binary_string=''
instruction_line_number_count=-1
variables_list_ld_st=[]

line_adjustment=-1

# Taking input file
for line in stdin:
    line=line.strip()
    if (line==''):
        #line_adjustment+=1
        list_of_instructions.append(line)
        continue

    instruction=line.split()
    
    list_of_instructions.append(instruction)

'''for i in list_of_instructions:
    print(i)'''

'''for instruction in list_of_instructions:
    if(instruction==''):
        list_of_instructions.remove(i)'''

for instruction in list_of_instructions:
    
    if(len(instruction)!=0):
        
        if(instruction[0]=='var'):
            line_number+=1
            memory_address_data[instruction[1]]=''
        
        if(len(instruction)>1 and instruction[1]==':'):
            line_number+=1
            print("Invalid label name because of space before ':' in line",list_of_instructions.index(instruction))
            exit(0)
        
        if(instruction[0][-1]==':'):
            len_of_label=len(instruction[0])-1
            instruction_line_number_count+=1
            num1=instruction_line_number_count
            labels[instruction[0][0:len_of_label:+1]]=bin8(num1)
            instruction_line_number_count+=-1
            instruction.pop(0)
            #continue
        if(instruction==[]):
            continue
        #print(instruction)
        #print("\n")
        if(instruction[0][-1].isalnum()):
            pass
        
        else:
            print("Invalid syntax at line",list_of_instructions.index(instruction))
            exit(0)
        
        if instruction[0] in type_A  :
            # reg1=instruction[1]
            # reg2=instruction[2]
            # reg3=instruction[3]
            # add(reg1,reg2,reg3,reg,output_list)
            instruction_line_number_count+=1
            line_number+=1
            #binary_string=TypeA(instruction)

        elif instruction[0] in type_B:
            # reg1=instruction[1]
            # reg2=instruction[2]
            # reg3=instruction[3]
            # sub(reg1,reg2,reg3,reg,output_list)
            try:
                
                if(instruction[0]=="mov" and instruction[2][0]=='$'):
                    instruction_line_number_count+=1
                    line_number+=1
                    #binary_string=TypeB(instruction)
                
                elif(instruction[0]=="mov" and instruction[2][0]!='$'):
                    #pass
                    instruction_line_number_count+=1
                    line_number+=1
                    #if()
                    #binary_string=TypeC(instruction)
                else:
                    instruction_line_number_count+=1
                    line_number+=1
                    #binary_string=TypeB(instruction)
                #elif
            except IndexError:
                print("Invalid syntax, less arguments passed in line",list_of_instructions.index(instruction))
                exit(0)


        elif instruction[0] in type_C:
            # '''reg1=instruction[1]
            # imm=instruction[2]
            # #reg3=instruction[3]
            # mov(reg1,imm,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1
            #binary_string=TypeC(instruction)

        elif instruction[0] in type_D:
            # '''reg1=instruction[1]
            # reg2=instruction[2]
            # #reg3=instruction[3]
            # mov(reg1,reg2,reg,output_list)'''
            #mem=instruction[1]
            try:
                variable=instruction[2]
                variables_list_ld_st.append(variable)
                instruction_line_number_count+=1
                line_number+=1
                #binary_string=TypeD(instruction)
            
            except IndexError:
                print("Invalid syntax, less arguments passed in line",list_of_instructions.index(instruction))
                exit(0)

        elif instruction[0] in type_E: 
            # '''mem1=instruction[2]
            # reg1=instruction[1]
            # #reg3=instruction[3]
            # ld(reg1,mem1,reg,output_list)'''
            #mem=instruction[1]
            instruction_line_number_count+=1
            line_number+=1
            #binary_string=TypeE(instruction)

        elif instruction[0] in type_F :
            # '''reg1=instruction[1]
            # mem1=instruction[2]
            # #reg3=instruction[3]
            # st(reg1,mem1,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1

        elif instruction[0] in type_G :
            # '''reg1=instruction[1]
            # mem1=instruction[2]
            # #reg3=instruction[3]
            # st(reg1,mem1,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1
            #binary_string=TypeF(instruction)
        
        elif instruction[0] in type_H :
            # '''reg1=instruction[1]
            # mem1=instruction[2]
            # #reg3=instruction[3]
            # st(reg1,mem1,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1
            #binary_string=TypeF(instruction)
        
        # '''var_after_instruction()
        # hlt_error()
        # check_error()'''
        # '''print("\n")
        # print("line number is ",line_number)
        # print("line adjustment is ",line_adjustment)
        # print("\n")'''
        #output_list.append(binary_string)

line_number=0
binary_string=''
instruction_line_number_count=-1
#variables_list_ld_st=[]

line_adjustment=-1

for instruction in list_of_instructions:
    
    if(len(instruction)!=0):
        
        if(instruction[0]=='var'):
            line_number+=1
            memory_address_data[instruction[1]]=''
        
        if(len(instruction)>1 and instruction[1]==':'):
            line_number+=1
            print("Invalid label name because of space before ':' in line",list_of_instructions.index(instruction))
            exit(0)
        
        if(instruction[0][-1]==':'):
            len_of_label=len(instruction[0])-1
            instruction_line_number_count+=1
            num1=instruction_line_number_count
            labels[instruction[0][0:len_of_label:+1]]=bin8(num1)
            instruction_line_number_count+=-1
            instruction.pop(0)
        
        if(instruction[0][-1].isalnum()):
            pass
        
        else:
            print("Invalid syntax at line",list_of_instructions.index(instruction))
            exit(0)
        
        if instruction[0] in type_A  :
            # reg1=instruction[1]
            # reg2=instruction[2]
            # reg3=instruction[3]
            # add(reg1,reg2,reg3,reg,output_list)
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeA(instruction)

        elif instruction[0] in type_B:
            # reg1=instruction[1]
            # reg2=instruction[2]
            # reg3=instruction[3]
            # sub(reg1,reg2,reg3,reg,output_list)
            try:
                
                if(instruction[0]=="mov" and instruction[2][0]=='$'):
                    instruction_line_number_count+=1
                    line_number+=1
                    binary_string=TypeB(instruction)
                
                elif(instruction[0]=="mov" and instruction[2][0]!='$'):
                    #pass
                    instruction_line_number_count+=1
                    line_number+=1
                    #if()
                    binary_string=TypeC(instruction)
                else:
                    instruction_line_number_count+=1
                    line_number+=1
                    binary_string=TypeB(instruction)
                #elif
            except IndexError:
                print("Invalid syntax, less arguments passed in line",list_of_instructions.index(instruction))
                exit(0)


        elif instruction[0] in type_C:
            # '''reg1=instruction[1]
            # imm=instruction[2]
            # #reg3=instruction[3]
            # mov(reg1,imm,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeC(instruction)

        elif instruction[0] in type_D:
            # '''reg1=instruction[1]
            # reg2=instruction[2]
            # #reg3=instruction[3]
            # mov(reg1,reg2,reg,output_list)'''
            #mem=instruction[1]
            try:
                variable=instruction[2]
                variables_list_ld_st.append(variable)
                instruction_line_number_count+=1
                line_number+=1
                binary_string=TypeD(instruction)
            
            except IndexError:
                print("Invalid syntax, less arguments passed in line",list_of_instructions.index(instruction))
                exit(0)

        elif instruction[0] in type_E: 
            # '''mem1=instruction[2]
            # reg1=instruction[1]
            # #reg3=instruction[3]
            # ld(reg1,mem1,reg,output_list)'''
            #mem=instruction[1]
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeE(instruction)

        elif instruction[0] in type_F :
            # '''reg1=instruction[1]
            # mem1=instruction[2]
            # #reg3=instruction[3]
            # st(reg1,mem1,reg,output_list)'''
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeF(instruction)

        elif instruction[0] in type_G  :
            #reg1=instruction[1]
            #reg2=instruction[2]
            #reg3=instruction[3]
            # add(reg1,reg2,reg3,reg,output_list)
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeG(instruction)

        elif instruction[0] in type_H  :
            #reg1=instruction[1]
            #reg2=instruction[2]
            #reg3=instruction[3]
            # add(reg1,reg2,reg3,reg,output_list)
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeH(instruction)
        
        # '''var_after_instruction()
        # hlt_error()
        # check_error()'''
        # '''print("\n")
        # print("line number is ",line_number)
        # print("line adjustment is ",line_adjustment)
        # print("\n")'''
        output_list.append(binary_string)

k=-1
#print("len of list\n",len(list_of_instructions))
#print("now printing again\n")
while(list_of_instructions[k]==''):
    #print("yes\n")
    list_of_instructions.pop(k)
    #k=k-1

# '''for i in list_of_instructions:
#     print(i)'''

instruction_line_number_count+=1

all=all+list(labels.keys())

var_after_instruction()
hlt_error()
check_error()

for key in memory_address_data:
    num=instruction_line_number_count
    memory_address_data[key]=bin8(num)
    instruction_line_number_count+=1

list_of_values=list(memory_address_data.values())

j=0
for i in range(len(output_list)):
    if(len(output_list[i])==8):
        output_list[i]=output_list[i]+memory_address_data[variables_list_ld_st[j]]
        instruction_line_number_count+=1
        j+=1

output_line=0
for i in output_list:
    if(output_line==256):
        print("Storage full! Output exceeding 256 lines")
        exit(0)
    output_line+=1
    print(i)
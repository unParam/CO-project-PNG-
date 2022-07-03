from re import T
from sys import stdin

def space_error(line):
    #i have a line like "hi i am   garv"
    #4 words
    #should have 3 spaces
    words=len(line.split())
    spaces=0
    for i in line:
        if i==" ":
            spaces+=1
    if spaces!=words-1:
        print("Invalid spaces in line number ") #line number
        exit(0)


def var_after_instruction():
    i=0
    while(list_of_instructions[i][0]=="var"):
        i=i+1
    for j in range(i,len(list_of_instructions)):
        if(list_of_instructions[j][0]=="var"):
            print("variable decleration after an instruction .. , they must be defined at the beginning") #line number
            exit(0)

def hlt_error():
    c=0
    for i in list_of_instructions:
        if i[0]=="hlt":
            c+=1
    if c>1:
        print("More than one hlt statements")
        exit(0)
    if list_of_instructions[-1][0]!="hlt":
        print("Last statement is not hlt")
        exit(0)


def error(l):
    
    if (l[0] != "var" and l[0] not in all):
        print("Invalid syntax in line number") #line number
        return True
    
    elif (l[0]=="var" and (l[1] in all or l[1][0].isdigit())):
        print("Invalid variable name at line")
        return True
    
    elif ((l[0]== 'jmp' or l[0] == 'jlt' or l[0] == 'jgt' or l[0] == 'je') and (l[1] in list(memory_address_data.keys()) or (l[1] in reg.keys() and l[0][1] !="FLAGS"))):
        print("Illegal memory address "+str(l[1]))
        return True
    
    # to check errors in A type instructions
    elif (l[0] == "add" or l[0] == "sub" or l[0] == "mul" or l[0] == "xor" or l[0] == "or" or l[0] == "and"):
        if (len(l) != 4):
            print("Wrong syntax used for instructions in line") #line number
            return True
        if(l[1]=="FLAGS" or l[2]=="FLAGS" or l[3]=="FLAGS"):
            print("Illegal use of flags register at line ") #line number
            return True
        elif (l[1] not in list(reg.keys()) or l[2] not in list(reg.keys()) or l[3] not in list(reg.keys())):
            print("Invalid register name in line") #line number
            return True

    # to check errors in both mov type instructions
    elif(l[0]=="mov"):
        if len(l)!=3:
            print("Wrong syntax used for instructions in line") #line number
            return True

        elif (l[1] == "FLAGS"):
            print("Illegal use of flags register at line ") #line number
            return True
        elif(l[2][1]=="R"):
            if(l[2] not in list(reg.keys())):
                print("Invalid register name in line ") #line number
                return True
        elif(l[2][1]=="$"):
            if (int(l[2][1:],10)<0 and int(l[2][1:],10)>255):
                print("Invalid immidiete in line "+str(l[1]))
                return True
    
    # to check errors in B type instructions
    elif ( l[0] == "rs" or l[0] == "ls"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions in line "+str(l[1]))
            return True
        if (l[1] == "FLAGS" or l[2]=="FLAGS"):
            print("Illegal use of flags register")
            return True
        elif (l[1] not in list(reg.keys())):
            print("Invalid register name in line")  #line number
            return True
        elif(l[2][1]=="$"):
            if (int(l[2][1:],10)<0 and int(l[2][1:],10)>255):
                print("Invalid immidiete in line "+str(l[1]))
                return True

    # to check errors in C type instructions
    elif (l[0]== "div" or l[0] == "not" or l[0] == "cmp"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions in line "+str(l[1]))
            return True
        if(l[1]=="FLAGS" or l[2]=="FLAGS"):
            print("Illegal use of flags register")
            return True
        elif (l[1] not in list(reg.keys()) or l[2] not in list(reg.keys())):
            print("Invalid register name in line "+str(l[1]))
            return True

    # to check errors in D type instructions
    elif (l[0] == "ld" or l[0] == "st"):
        if (len(l) != 3):
            print("Wrong syntax used for instructions in line "+str(l[1]))
            return True
        elif(l[1]=="FLAGS"):
            print("Illegal use of flags register")
            return True
        elif (l[1] not in list(reg.keys())):
            print("Invalid register name in line "+str(l[1]))
            return True
        elif l[2] not in list(memory_address_data.keys()):
            print("Invalid memory address in line "+str(l[1]))
            return True
    
    # to check errors in E type instructions
    elif (l[0] == "jmp" or l[0] == "jlt" or l[0] == "jgt" or l[0] == "je"):
        if (len(l) != 2):
            print("Wrong syntax used for instructions in line "+str(l[1]))
            return True
        if l[1] not in list(labels.keys()):
            print("Invalid  memory address in line "+str(l[1]))
            return True
    
    # to check errors in F type instructions
    elif (l[0] == "hlt"):
        if (len(l) != 1):
            print("Wrong syntax used for instructions in line "+str(l[1]))
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
        
    s+="0"*2+reg[L[1]][0]+reg[L[2]][0]+reg[L[3]][0]
    return s

def TypeB(L):
    if L[0]=="mov":
        s="10010"
        #reg[L[1]][1]=L[2][1:]

    elif L[0]=="rs":
        s="11000"
        '''imm_in_binary=str(bin8(int(L[2][1:])))
        imm_in_decimal=bin(imm_in_binary)[2:]
        imm_in_binary=int(imm_in_binary)
        reg1=reg[L[1]][1]
        reg1=imm_in_binary
        reg[L[1]][1]=reg1'''

    elif L[0]=="ls":
        s="11001"
        '''imm_in_binary=str(bin8(int(L[2][1:])))
        imm_in_decimal=bin(imm_in_binary)[2:]
        imm_in_binary=int(imm_in_binary)
        reg1=reg[L[1]][1]
        reg1=imm_in_binary
        reg[L[1]][1]=reg1'''
        
    s+=reg[L[1]][0]+bin8(int(L[2][1:]))
    return s

def TypeC(L):
    
    if L[0]=="mov":
        s="10011"
        '''reg1=reg[L[1]][1]
        reg2=reg[L[2]][1]
        reg2=reg1
        reg[L[2]][1]=reg2'''

    elif L[0]=="div":
        s="10111"
        '''reg1=reg[L[1]][1]
        reg0=reg[L[0]][1]
        reg3=reg[L[3]][1]
        reg4=reg[L[4]][1]
        reg0=reg3//reg4
        reg1=reg3%reg4'''

        '''reg[L[0]][1]=reg0
        reg[L[1]][1]=reg1'''

    elif L[0]=="not":
        s="11101"
        '''reg1=reg[L[1]][1]
        reg2=reg[L[2]][1]
        reg2=~reg1
        reg[L[2]][1]=reg2'''

    elif L[0]=="cmp":          #to be changed  !!
        s="11110"
        '''reg1=reg[L[1]][1]
        reg2=reg[L[2]][1]'''
        
        '''if(reg1>reg2):
            reg['flags'][1][-2]=1
        elif(reg1<reg2):
            reg['flags'][1][-3]=1
        elif(reg1==reg2):
            reg['flags'][1][-1]=1'''
        

    s+="0"*5+reg[L[1]][0]+reg[L[2]][0]
    return s

def TypeD(L):
    if L[0]=="ld":
        s="10100" 
        '''reg1=reg[L[1]][1]
        val=memory_address_data[L[2]]
        reg1=val
        reg[L[1]][1]=reg1'''
        
    elif L[0]=="st":
        s="10101"
        '''reg1=reg[L[1]][1]
        memory_address_data[L[2]]=reg1
        reg[L[1]][1]=reg1'''

    address=memory_address_data[L[2]]

    s+=reg[L[1]][0]+address
    return s



def TypeE(L):              #to be done !!
    if L[0]=="jmp":
        s="11111"
        
              
    elif L[0]=="jlt":
        s="01100"

    elif L[0]=="jgt":
        s="01101"

    elif L[0]=="je":
        s="01111"

    address=labels[L[1]]
    #s+="0"*3+L[1]
    s+="0"*3+address
    return s

def TypeF(L):  #this is halt(hlt)
    s="01010"+"0"*11
    return s



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

all_inst = type_A+type_B+type_C+type_D+type_E+type_F


memory_address_data={}
labels={}
list_of_instructions=[]
output_list=[]
line_number=0
binary_string=''
instruction_line_number_count=-1
variables_list_ld_st=[]

for line in stdin:
    line=line.strip()
    '''if line=="hlt":
        break'''
    space_error(line)
    instruction=line.split()
    list_of_instructions.append(instruction)

for instruction in list_of_instructions:
    if(len(instruction)==0):
        break
    if(instruction[0]=='var'):
        line_number+=1
        memory_address_data[instruction[1]]=''

    if(instruction[0][-1]==':'):
        len_of_label=len(instruction[0])-1
        num1=line_number
        labels[instruction[0][0:len_of_label:+1]]=bin8(num1)#line_number
        instruction.pop(0)
    if instruction[0] in type_A  :
        '''reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3,reg,output_list)'''
        instruction_line_number_count+=1
        line_number+=1
        binary_string=TypeA(instruction)

    elif instruction[0] in type_B:
        '''reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        sub(reg1,reg2,reg3,reg,output_list)'''
        if(instruction[0]=="mov" and instruction[2][0]=='$'):
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeB(instruction)
        elif(instruction[0]=="mov" and instruction[2][0]!='$'):
            pass
        else:
            instruction_line_number_count+=1
            line_number+=1
            binary_string=TypeB(instruction)


    elif instruction[0] in type_C:
        '''reg1=instruction[1]
        imm=instruction[2]
        #reg3=instruction[3]
        mov(reg1,imm,reg,output_list)'''
        instruction_line_number_count+=1
        line_number+=1
        binary_string=TypeC(instruction)

    elif instruction[0] in type_D:
        '''reg1=instruction[1]
        reg2=instruction[2]
        #reg3=instruction[3]
        mov(reg1,reg2,reg,output_list)'''
        #mem=instruction[1]
        variable=instruction[2]
        variables_list_ld_st.append(variable)
        instruction_line_number_count+=1
        line_number+=1
        binary_string=TypeD(instruction)

    elif instruction[0] in type_E: 
        '''mem1=instruction[2]
        reg1=instruction[1]
        #reg3=instruction[3]
        ld(reg1,mem1,reg,output_list)'''
        #mem=instruction[1]
        instruction_line_number_count+=1
        line_number+=1
        binary_string=TypeE(instruction)

    elif instruction[0] in type_F :
        '''reg1=instruction[1]
        mem1=instruction[2]
        #reg3=instruction[3]
        st(reg1,mem1,reg,output_list)'''
        
        instruction_line_number_count+=1
        line_number+=1
        binary_string=TypeF(instruction)

    #instruction_line_number_count+=-1
    

    output_list.append(binary_string)

instruction_line_number_count+=1
for key in memory_address_data:
    num=instruction_line_number_count
    memory_address_data[key]=bin8(num)
    instruction_line_number_count+=1

'''d1={1:1,2:3,3:4}
l=list(d1.values())'''

list_of_values=list(memory_address_data.values())



j=0
for i in range(len(output_list)):
    if(len(output_list[i])==8):
        output_list[i]=output_list[i]+memory_address_data[variables_list_ld_st[j]]#list_of_values[j] #bin8(instruction_line_number_count)
        instruction_line_number_count+=1
        j+=1

'''for i in range(len(output_list)):
    if(len(output_list[i])==9):
        output_list[index(i)]=i+list_of_values[j] #bin8(instruction_line_number_count)
        instruction_line_number_count+=1
        j+=1'''

for i in output_list:
    print(i)
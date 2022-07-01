def 

from sys import stdin

#reg_value_dict = {"R0" : 0, "R1" : 0, "R2" : 0, "R3" : 0, "R4" : 0, "R5" :0, "R6" : 0, "FLAGS" : "0000"}
#op_code_dict = {"R0" : "000", "R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110", "FLAGS" : "111"}
reg_name_list = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
vars_dict={}
reg_dict_combined = {'R0': ['000', 0],
       'R1': ['001', 0],
       'R2': ['010', 0],
       'R3': ['011', 0],
       'R4': ['100', 0],
       'R5': ['101', 0],
       'R6': ['110', 0],
       'FLAGS': ['111', 0]}

list1=[]
output_list=[]
for line in stdin:
    list2=line.split()
    list1.append(list2)

for instruction in list1:
    if(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3,reg,output_list)
    elif(instruction[0]=="sub"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        sub(reg1,reg2,reg3,reg,output_list)
    elif(instruction[0]=="mov" and instruction[2][0]=='$'):
        reg1=instruction[1]
        imm=instruction[2]
        #reg3=instruction[3]
        mov(reg1,imm,reg,output_list)
    elif(instruction[0]=="mov"):
        reg1=instruction[1]
        reg2=instruction[2]
        #reg3=instruction[3]
        mov(reg1,reg2,reg,output_list)
    elif(instruction[0]=="ld"):
        mem1=instruction[2]
        reg1=instruction[1]
        #reg3=instruction[3]
        ld(reg1,mem1,reg,output_list)
    elif(instruction[0]=="st"):
        reg1=instruction[1]
        mem1=instruction[2]
        #reg3=instruction[3]
        st(reg1,mem1,reg,output_list)
    elif(instruction[0]=="mul"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        mul(reg1,reg2,reg3,reg)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    elif(instruction[0]=="add"):
        reg1=instruction[1]
        reg2=instruction[2]
        reg3=instruction[3]
        add(reg1,reg2,reg3)
    






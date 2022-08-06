# regfile[r1]=110 10100

# 110 10100
# exp=6
# true exp= 6-x maybe x=3
# true exp=3
# 1.mantissa * 2**(true exp)
# for shifting, (1.mantissa)* 10**truexp
# -> suppose (0.011) base 2
# to int using bin funcn, inbuilt wale

def f(s):
    s=str(s)
    a,b=s.split(".")
    a=a[::-1]
   

    lt=0
    rt=0
    for i in range(len(a)):
        lt=lt+(int(a[i]))*(2**i)
    for j in range(1,len(b)+1):
        rt=rt+(int(b[j-1]))*(2**(-j))

    ans=float(lt+rt)
    return ans

def floatbinright_to_floatdec(s):
    ans=0
    for i in range(1,len(s[2:])+1):
        ans=ans+int(s[i+1])*(2**(-i))
    ans=str(ans)
    ans=ans[2:]
    return ans


from sys import stdin
#import matplotlib.pyplot as plt
#import numpy as np

mem=['0000000000000000\n']*256 #initialising memory

reg_str_data=['0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000']

pc=0
reg_file=[0]*8
halt=False
ins_list=[]
x_arr=[]
y_arr=[]
cycle=0

def binarytodecimal(str1):
    str1=str(str1)
    lenstr1=len(str1)
    decimal=0
    count=0
    while lenstr1>0:
        decimal+=(2**(lenstr1-1)*(int(str1[count])))
        lenstr1-=1
        count+=1
    return str(decimal)

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

'''def floatoctal_convert(my_number, places = 3):
   my_whole, my_dec = str(my_number).split(".")
   my_whole = int(my_whole)
   my_dec = int (my_dec)
   res = bin(my_whole).lstrip("0b") + "."
   for x in range(places):
      my_whole, my_dec = str((my_decimal_converter(my_dec)) * 8).split(".")
      my_dec = int(my_dec)
      res += my_whole
   return res
def my_decimal_converter(num):
   while num > 1:
      num /= 10
   return num'''

def bin16(n):    #converts an integer to an 16-bit binary number

    binary=bin(n)[2:]                      #Since bin() prefixes "0b", so we remove it by slicing it out.     
    binary=("0"*(16-len(binary)))+binary    #If the binary part in previous step is not 16-bit , then we have to add extra zeroes in the front.
    return binary[0:16]  



def convert_afterdec(n):
    n=float(n)
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

def addf(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)


    #r1_data=reg_file[r_1]
    '''if(isinstance(r1_data,int)):
        print("Invalid data in reg: trying to add int instead of float")
        exit(0)'''
    #r1_binary=bin16(r1_data)
    #r1_exp=r1_binary[8:11]
    #r1_mantissa=r1_binary[11:16]

    #r2_data=reg_file[r_2]

    r1_data=reg_str_data[r_1]
    r2_data=reg_str_data[r_2]

    r1_data=r1_data[8:]
    r2_data=r2_data[8:]

    r1_exp=r1_data[0:3]
    r2_exp=r2_data[0:3]

    r1_man=r1_data[3:]
    r2_man=r2_data[3:]

    a=(float('1'+"."+r1_man))*(10**(int(r1_exp,2)))
    b=(float('1'+"."+r2_man))*(10**(int(r2_exp,2)))

    '''111.11
    7.75
'''
    flg=0
    a=f(a)
    b=f(b)

    ans=a+b
    if(ans>252):
        reg_str_data[r_sto]='0000000011111111'
        reg_file[r_sto]=255
        reg_file[7]=8
        '''global pc
        pc +=1
        return'''
        flg=1
    if(flg!=1):
        ans=str(ans)

        lt,rt=ans.split('.')
        # 5   .   75
        #len_lt=len(lt)
        #len_rt=len(rt)

        #print(lt)
        lt=decimaltobinary(lt)
        
        #print(rt)
        if(rt!='0'):
            rt='0.'+rt
            rt=float(rt)
            rt=convert_afterdec(rt)
        
        #else:

        ans=lt+'.'+rt
        ans=float(ans)
        len_lt=len(lt)

        ans=ans*(10**-(len_lt-1))

        ans=str(ans)

        man=ans[2:7]
        while(len(man)!=5):
            man=man+'0'
        exp=decimaltobinary(len_lt-1)
        while(len(exp)!=3):
            exp='0'+exp

        reg_str_data[r_sto]=exp+man
        #print(reg_str_data[r_sto])
        reg_file[r_sto]=binarytodecimal(reg_str_data[r_sto])

        #if(isinstance(r1_data,float) or )
        '''if(isinstance(r2_data,int)):
            print("Invalid data in reg: trying to add int instead of float")
            exit(0)'''
        #r2_binary=bin16(r2_data)
        #r2_exp=r2_binary[8:11]
        #r2_mantissa=r2_binary[11:16]

        #r1_dec="1."+r1_mantissa
        '''r1_dec=int(r1_dec)
        r1_dec=(r1_dec)*((10)**r1_exp)
        r1_dec=int(r1_dec,2)

        r2_dec="1."+r2_mantissa
        r2_dec=int(r2_dec)
        r2_dec=(r2_dec)*((10)**r2_exp)
        r2_dec=int(r2_dec,2)'''

        '''sum_dec=r1_data+r2_data


        #sum_reg = reg_file[r_1] + reg_file[r_2]
        #if sum_dec <= 15.75:
        if sum_dec <= 252:

            reg_file[r_sto]=sum_dec
            sum_left_dec, sum_right_dec = str(sum_dec).split(".")
            sum_left_dec=decimaltobinary(sum_left_dec)
            sum_right_dec='0.'+sum_right_dec
            sum_right_dec=int(sum_right_dec)
            sum_right_dec=convert_afterdec(sum_right_dec)

            sum_bin=sum_left_dec+'.'+sum_right_dec
            sum_bin=int(sum_bin)

            reg_file[7] = 0
            reg_str_data[7]="0000000000000000" 
            #len_left=len(sum_left_dec)
            #x=sum_bin*(10**(-len_left+1))
            #exp=0
            #mantissa=x[]
            #for i in range(len_left-1):
        else:
            reg_file[7]=8 
            reg_str_data[7]="0000000000001000"  '''   
    #01001.111 
    #x =1.00111

    # 1.11111 * 2^111

            #reg_file[r_sto] = sum_reg
            #reg_file[7] = 0

        '''else:
            sum_reg =  sum_reg & 65535
            reg_file[r_sto] = sum_reg
            reg_file[7] = 8'''
    
    global pc
    pc +=1

def subf(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)

    r1_data=reg_str_data[r_1]
    r2_data=reg_str_data[r_2]

    r1_data=r1_data[8:]
    r2_data=r2_data[8:]

    r1_exp=r1_data[0:3]
    r2_exp=r2_data[0:3]

    r1_man=r1_data[3:]
    r2_man=r2_data[3:]

    a=(float('1'+"."+r1_man))*(10**(int(r1_exp,2)))
    b=(float('1'+"."+r2_man))*(10**(int(r2_exp,2)))

    '''111.11
    7.75
'''

    a=f(a)
    b=f(b)
    flg=0
    ans=a-b

    #print("ans is ",ans)
    if(ans<1):
        reg_str_data[r_sto]='0000000000000000'
        reg_file[r_sto]=0
        reg_file[7]=8
        '''global pc
        pc +=1
        return'''
        flg=1
    ans=str(ans)

    if(flg!=1):
        lt,rt=ans.split('.')
        # 5   .   75
        #len_lt=len(lt)
        #len_rt=len(rt)

        #print(lt)
        lt=decimaltobinary(lt)
        if(rt!='0'):
            rt='0.'+rt
            rt=float(rt)
            rt=convert_afterdec(rt)

        ans=lt+'.'+rt
        ans=float(ans)
        #print("ans is ",ans)
        len_lt=len(lt)

        ans=ans*(10**(-len_lt+1))

        ans=str(ans)
        #print("ans is ",ans)
        #print(ans)
        man=ans[2:7]
        while(len(man)!=5):
            man=man+'0'
        
        exp=decimaltobinary(str(int(len_lt-1)))
        while(len(exp)!=3):
            exp='0'+exp

        reg_str_data[r_sto]=exp+man
        #print(reg_str_data[r_sto])
        reg_file[r_sto]=binarytodecimal(reg_str_data[r_sto])

        #r1_data=reg_file[r_1]
        '''if(isinstance(r1_data,int)):
            print("Invalid data in reg: trying to add int instead of float")
            exit(0)'''
        #r1_binary=bin16(r1_data)
        #r1_exp=r1_binary[8:11]
        #r1_mantissa=r1_binary[11:16]

        #r2_data=reg_file[r_2]
        '''if(isinstance(r2_data,int)):
            print("Invalid data in reg: trying to add int instead of float")
            exit(0)'''
        #r2_binary=bin16(r2_data)
        #r2_exp=r2_binary[8:11]
        #r2_mantissa=r2_binary[11:16]

        #r1_dec="1."+r1_mantissa
        '''r1_dec=int(r1_dec)
        r1_dec=(r1_dec)*((10)**r1_exp)
        r1_dec=int(r1_dec,2)

        r2_dec="1."+r2_mantissa
        r2_dec=int(r2_dec)
        r2_dec=(r2_dec)*((10)**r2_exp)
        r2_dec=int(r2_dec,2)'''

        '''sum_dec=r1_data-r2_data


        #sum_reg = reg_file[r_1] + reg_file[r_2]
        #if sum_dec <= 15.75:
        if 0<=sum_dec <= 252:

            reg_file[r_sto]=sum_dec
            sum_left_dec, sum_right_dec = str(sum_dec).split(".")
            sum_left_dec=decimaltobinary(sum_left_dec)
            sum_right_dec='0.'+sum_right_dec
            sum_right_dec=int(sum_right_dec)
            sum_right_dec=convert_afterdec(sum_right_dec)

            sum_bin=sum_left_dec+'.'+sum_right_dec
            sum_bin=int(sum_bin)

            reg_file[7] = 0
            reg_str_data[7]="0000000000000000" 
            #len_left=len(sum_left_dec)
            #x=sum_bin*(10**(-len_left+1))
            #exp=0
            #mantissa=x[]
            #for i in range(len_left-1):
        else:
            reg_file[7]=8
            reg_str_data[7]="0000000000001000"  '''    
    #01001.111 
    #x =1.00111

    # 1.11111 * 2^111

            #reg_file[r_sto] = sum_reg
            #reg_file[7] = 0

        '''else:
            sum_reg =  sum_reg & 65535
            reg_file[r_sto] = sum_reg
            reg_file[7] = 8'''
    try:
        global pc
        pc +=1
    except:
        return


def movf(s):
    r_sto = int(s[5:8],2)
    #imm = s[8:16]
    #r2_binary=bin16(r2_data)
    r1_exp=s[8:11]
    r1_mantissa=s[11:16]

    reg_str_data[r_sto]='00000000'+r1_exp+r1_mantissa

    reg_file[r_sto]=binarytodecimal(int(reg_str_data[r_sto]))

    '''r1_exp=int(r1_exp,2)

    r1_dec="1."+r1_mantissa
    r1_dec=float(r1_dec)
    r1_dec=(r1_dec)*((10)**r1_exp)
    #r1_dec=int(r1_dec,2)
    r1_dec=float(r1_dec)
    #print("r1 is ",r1_dec)

    sum_left_dec, sum_right_dec = str(r1_dec).split(".")
    #len_rt=len(sum_right_dec)
    sum_left_dec=binarytodecimal(sum_left_dec)
    #print("sum left",sum_left_dec)
    sum_right_dec='0.'+sum_right_dec
    #sum_right_dec=float(sum_right_dec)
    sum_right_dec=floatbinright_to_floatdec(sum_right_dec)
    #print("sum right",sum_right_dec)
    #sum_right_dec=str(sum_right_dec)
    len_rt=len(sum_right_dec)

    

    sum_bin=sum_left_dec+'.'+sum_right_dec
    sum_bin=float(sum_bin)'''

    '''sum_left_dec, sum_right_dec = str(sum_bin).split(".")
    #len_rt=len(sum_right_dec)
    sum_left_dec=binarytodecimal(sum_left_dec)
    #print("sum left",sum_left_dec)
    sum_right_dec='0.'+sum_right_dec
    #sum_right_dec=float(sum_right_dec)
    sum_right_dec=floatbinright_to_floatdec(sum_right_dec)
    #print("sum right",sum_right_dec)
    #sum_right_dec=str(sum_right_dec)
    len_rt=len(sum_right_dec)'''

    '''if(sum_bin<=252):
        #print("final stored value: ",sum_bin)
        reg_file[r_sto] = sum_bin
        reg_file[7] = 0
        reg_str_data[7]="0000000000000000" 
    
    else:
        reg_file[7] = 8
        reg_str_data[7]="0000000000001000" '''
    '''r2_dec="1."+r2_mantissa
    r2_dec=int(r2_dec)
    r2_dec=(r2_dec)*((10)**r2_exp)
    r2_dec=int(r2_dec,2)'''
    #reg_file[r_sto] = imm
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000"

def load(s):    
    reg=int(s[5:8],2)
    mem_add=int(s[8:],2)
    reg_file[reg]=int(mem[mem_add],2)
    reg_str_data[reg]=bin16(int(mem[mem_add],2))
    #reg_str_data
    global pc
    pc+=1
    reg_file[7]=0
    reg_str_data[7]="0000000000000000" 
    x_arr.append(cycle)
    y_arr.append(mem_add)

def store(s):
    reg=int(s[5:8],2)
    mem_add=int(s[8:],2)
    #if(isinstance(reg_file[reg],float)):

    val=convertBin(reg_file[reg],16)
    mem[mem_add]=val
    global pc
    pc+=1
    reg_file[7]=0 
    reg_str_data[7]="0000000000000000" 
    x_arr.append(cycle)
    y_arr.append(mem_add)


def rs(s):
    reg=int(s[5:8],2)
    imm=int(s[8:],2)
    reg_file[reg]=reg_file[reg]>>imm
    reg_str_data[reg]=bin16(reg_file[reg])
    global pc
    pc+=1
    reg_file[7]=0
    reg_str_data[7]="0000000000000000" 
    
    
def ls(s):
    reg=int(s[5:8],2)
    imm=int(s[8:],2)
    reg_file[reg]=reg_file[reg]<<imm
    reg_str_data[reg]=bin16(reg_file[reg])
    global pc
    pc+=1
    reg_file[7]=0
    reg_str_data[7]="0000000000000000" 
    
    
def cmp(s):
    reg1=int(s[10:13],2)
    reg2=int(s[13:],2)
    reg_file[7]=0
    val1=reg_file[reg1]
    val2=reg_file[reg2]
    if(val1==val2):
        reg_file[7]=1
        reg_str_data[7]='0000000000000001'
    elif(val1>val2):
        reg_file[7]=2
        reg_str_data[7]='0000000000000010'
    else:
        reg_file[7]=4
        reg_str_data[7]='0000000000000100'
    global pc
    pc+=1

def jmp(s):
    global pc
    mem_add=int(s[8:],2)
    pc=mem_add
    reg_file[7]=0 
    reg_str_data[7]="0000000000000000" 

def jgt(s):
    global pc
    if(reg_file[7]==2):
        mem_add=int(s[8:],2)
        pc=mem_add 
        
    else :
        pc+=1    
    reg_file[7]=0
    reg_str_data[7]='0000000000000000'
         
    
def jlt(s):
    global pc
    if(reg_file[7]==4):
        mem_add=int(s[8:],2)
        pc=mem_add 
    else:
        pc+=1
    reg_file[7]=0
    reg_str_data[7]='0000000000000000'
    

def je(s):
    global pc
    if(reg_file[7]==1):
        mem_add=int(s[8:],2)
        pc=mem_add  
    else:
        pc+=1
    reg_file[7]=0
    reg_str_data[7]='0000000000000000'

def add(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)
    sum_reg = reg_file[r_1] + reg_file[r_2]
    if sum_reg <= 65535:
        reg_file[r_sto] = sum_reg
        reg_str_data[r_sto]=bin16(sum_reg)
        reg_file[7] = 0
        reg_str_data[7]='0000000000000000'
    else:
        sum_reg =  sum_reg & 65535
        reg_file[r_sto] = sum_reg
        reg_str_data[r_sto]=bin16(sum_reg)
        reg_file[7] = 8
        reg_str_data[7]='0000000000001000'
    global pc
    pc +=1
    
    
def sub(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)
    sub_reg = reg_file[r_1] - reg_file[r_2]
    if sub_reg >= 0:
        reg_file[r_sto] = sub_reg
        reg_str_data[r_sto]=bin16(sub_reg)
        reg_file[7] = 0
        reg_str_data[7]='0000000000000000'
    else:
        reg_file[r_sto] = sub_reg
        reg_str_data[r_sto]=bin16(sub_reg)
        reg_file[7] = 8
        reg_str_data[7]='0000000000001000'
    global pc
    pc +=1
    
    
def mov_im(s):
    r_sto = int(s[5:8],2)
    imm = int(s[8:16],2)
    reg_file[r_sto] = imm
    reg_str_data[r_sto]=bin16(imm)
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]='0000000000000000'
  
    
def mov_reg(s):
    r_sto = int(s[10:13],2)
    r_1 = int(s[13:16],2)
    #reg_file[r_sto] = reg_file[r_1]
    reg_file[r_1] = reg_file[r_sto]
    reg_str_data[r_1]=bin16(reg_file[r_sto])
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    
    
def mul(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)
    pro_reg = reg_file[r_1] * reg_file[r_2]
    if pro_reg <= 65535:
        reg_file[r_sto] = pro_reg
        reg_str_data[r_sto]=bin16(pro_reg)
        reg_file[7] = 0
        reg_str_data[7]="0000000000000000" 
    else:
        pro_reg =  pro_reg & 65535
        reg_file[r_sto] = pro_reg
        reg_str_data[r_sto]=bin16(pro_reg)
        reg_file[7] = 8
        reg_str_data[7]="0000000000001000" 
    global pc
    pc +=1
    
def div(s):
    r_1 = int(s[10:13],2)
    r_2 = int(s[13:16],2)
    reg_file[0] = (reg_file[r_1])//(reg_file[r_2])
    reg_str_data[0]=bin16((reg_file[r_1])//(reg_file[r_2]))
    reg_file[1] = (reg_file[r_1])%(reg_file[r_2])
    reg_str_data[1]=bin16((reg_file[r_1])%(reg_file[r_2]))
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    
def Or(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)
    or_reg = (reg_file[r_1])|(reg_file[r_2])
    reg_file[r_sto] = or_reg
    reg_str_data[r_sto]=bin16(or_reg)
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    
def And(s):
    r_1 = int(s[7:10],2)
    r_2 = int(s[10:13],2)
    r_sto = int(s[13:16],2)
    and_reg = (reg_file[r_1])&(reg_file[r_2])
    reg_file[r_sto] = and_reg
    reg_str_data[r_sto]=bin16(and_reg)
    
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    
def invert(s):
    # r_sto = int(s[10:13],2)
    r_1 = int(s[10:13],2)
    r_2 = int(s[13:16],2)
    r_sto = r_2
    x = reg_file[r_1]
    
    """
    x = bin(x)
    x = x[2:]
    l = len(x)
    x = "0"*(16-l) + x
    not_x = ""
    for i in range(0, len(x)):
        if x[i] == "0":
            not_x = not_x + "1"
        else:
            not_x = not_x + "0"
    
    not_reg = int(not_x,2)
    """
    not_reg = 65535-x
    #not_reg = ~x
    reg_file[r_sto] = not_reg
    reg_str_data[r_sto]=bin16(not_reg)
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    
def xor(s):
    r_sto = int(s[7:10],2)
    r_val=reg_file[r_sto]
    not_rsto=65535-r_val
    r_1 = int(s[10:13],2)
    r1_val = reg_file[r_1]
    not_r1 = 65535 - r1_val
    r_2 = int(s[13:16],2)
    r2_val = reg_file[r_2]
    not_r2 = 65535 - r2_val
    xor_reg = ((r1_val)&(not_rsto))|((not_r1)&r_val)
    reg_file[r_2] = xor_reg
    reg_str_data[r_2]=bin16(xor_reg)
    global pc
    pc +=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 

def hlt(s):
    global pc
    pc+=1
    reg_file[7] = 0
    reg_str_data[7]="0000000000000000" 
    global halt
    halt=True    
    

op_dict={"10000":add,"10001":sub,"10010":mov_im,
         "10011":mov_reg,"10100":load,"10101":store,"10110":mul,"10111":div,
         "11000":rs,"11001":ls,"11010":xor,"11011":Or,"11100":And,"11101":invert,
         "11110":cmp,"11111":jmp,"01100":jlt,"01101":jgt,"01111":je,"01010":hlt,"00000":addf,"00001":subf,"00010":movf}
    
    
def convertBin(n,b):
    y=bin(int(n))
    if y[0] == "-":
        y = y[3:]
        l = len(y)
        y = "0"*(b-l) + str(y)
    else:
        y=y[2:]
        l=len(y)
        y="0"*(b-l)+ str(y)
    return y
    



# fi = open('co.txt', 'r+')
# ins_list = fi.read()
# ins_list = ins_list.split('\n')
   


for line in stdin:
    ins_list.append(line)


#print(ins_list)
for i in ins_list:
    if(i=='\n'):
        ins_list.remove(i)

#print('\n')
#print('\n')

'''print(len(ins_list))

print('\n')
print('\n')
print(ins_list)
print(len(ins_list))'''

    
for i in range(0,len(ins_list)):
    mem[i]=ins_list[i]
    

while(halt==False):
    cycle+=1
    x_arr.append(cycle)
    curr_ins=mem[pc]
    y_arr.append(pc)
    print(convertBin(pc,8), end=" ")
    op_dict[curr_ins[0:5]](curr_ins)
    for i in reg_file:
        if(isinstance(i,float)):
            sum_left_dec, sum_right_dec = str(i).split(".")
            #len_rt=len(sum_right_dec)
            sum_left_dec=decimaltobinary(sum_left_dec)
            sum_right_dec='0.'+sum_right_dec
            sum_right_dec=float(sum_right_dec)
            sum_right_dec=convert_afterdec(sum_right_dec)
            len_rt=len(sum_right_dec)
            #print("sum left",sum_left_dec)
            #print("sum right",sum_right_dec)
            sum_bin=sum_left_dec+'.'+sum_right_dec
            sum_bin=float(sum_bin)
            #print("sumbin is ",sum_bin)
            
            exp=0

            mantissa=len(sum_left_dec)-1
            sum_bin=sum_bin*(10**(-mantissa))
            exp=mantissa

            if(len_rt+mantissa>5):
                print("final error more than 5 mantissa bits")
                exit(0)

            str1=str(sum_bin)
            #print("str1 is ",str1)
            str1=str1[2:]
            #print("now str1 is ",str1)
            while(len(str1)!=5):
                str1=str1+'0'
            if(exp>7 or exp<0):
                print("final invalid exponent")
                exit(0)

            str2=decimaltobinary(exp)
            while(len(str2)!=3):
                str2='0'+str2
            #print("str2 is ",str2)
            str3=str2+str1
            while(len(str3)!=16):
                str3='0'+str3
            print(str3,end=' ')
            continue

        print(convertBin(i,16),end=" ")
    print("")
#plt.scatter(x_arr, y_arr)
#plt.show()
   

for i in mem:
    #print(i,end='')
    print(i)
#print(*mem,sep='\n')
#print(len(mem))
# fi.close()
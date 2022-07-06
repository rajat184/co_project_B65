myDict = {
    'add': ('10000', 'A'), 'sub': ('10001', 'A'),
    'movI': ('10010', 'B'), 'movR': ('10011', 'C'),
    'ld': ('10100', 'D'), 'st': ('10101', 'D'),
    'mul': ('10110', 'A'), 'div': ('10111', 'C'),
    'rs': ('11000', 'B'), 'ls': ('11001', 'B'),
    'xor': ('11010', 'A'), 'or': ('11011', 'A'),
    'and': ('11100', 'A'), 'not': ('11101', 'C'),
    'cmp': ('11110', 'C'), 'jmp': ('11111', 'E'),
    'jlt': ('01100', 'E'), 'jgt': ('01101', 'E'),
    'je': ('01111', 'E'), 'hlt': ('01010', 'F')
}

file=open("stdout.txt","w")

myReg = {
    'R0': '000', 'R1': '001', 'R2': '010',
    'R3': '011', 'R4': '100', 'R5': '101',
    'R6': '110', 'FLAGS': '111'
}

label = {}   # empty dictionary

def dec2bin(ans):
    res = '{0:08b}'.format(ans)
    return res

def countline():          # just returning the list of list of all the items 

    filenames = []
    list = []

    with open("stdin.txt", "r") as file:
        for line in file:
            line = line.strip()  # remove any trailing/leading spaces
            line = line.strip('"')  # remove wrapping quotes
            if line:  # if there still is content...
                filenames.append(line)  # save the valid line.

    for line in filenames:
        list.append(line.split())
    
    return list

dict = {}

global word

def checkline2bin(cmnd):
    count = 0
    z = countline()
    
    flag = 0
    for i in z:
        count += 1
        for j in i:

            if j == cmnd:
                flag = 1
                global word
                word = (i[-1])
                break
            
        if flag == 1:
            break

    dict[word] = count   
    ans=dec2bin(count)
    return str(ans)

def add(cmd):
    op = "add"
    str = ""
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def sub(cmd):
    op = "sub"
    str = ''
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def mul(cmd):
    op = "mul"
    str = ''
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def cmp(cmd):
    op = "cmp"
    str = ""
    str = myDict[op][0] + '00000' + myReg[cmd[1]] + myReg[cmd[2]]
    return str

def mov(cmd):
    if(cmd[-1][0] == '$'):
        res = int(cmd[-1][1:])
        s = "10010" + myReg[cmd[1]] + dec2bin(res)
    else:
        s = "10011" + "00000" + myReg[cmd[1]] + myReg[cmd[2]]
    return s

def hlt():
    op = "hlt"
    str = ""
    str = myDict[op][0] + '00000000000'
    return str

def div(cmd):
    op = "div"
    str = ""
    str = myDict[op][0] + '00000' + myReg[cmd[1]] + myReg[cmd[2]]
    return str

def ls(cmd):
    op = "ls"
    str = ""
    k = int(cmd[-1][1:])
    str = myDict[op][0] + myReg[cmd[1]] + dec2bin(k)
    return str

def rs(cmd):
    op="rs"
    str=""
    k=int(cmd[-1][1:])
    str = myDict[op][0] + myReg[cmd[1]] + dec2bin(k)
    return str
    
def Not(cmd):
    op = "not"
    str = myDict[op][0] + '00000' + myReg[cmd[1]] + myReg[cmd[2]]
    return str

def xor(cmd):
    op = "xor"
    str = ""
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def OR(cmd):
    op = "or"
    str = ""
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def And(cmd):
    op = "and"
    str = ""
    str = myDict[op][0] + '00' + myReg[cmd[1]] + myReg[cmd[2]] + myReg[cmd[3]]
    return str

def jmp(cmd):
    op="jmp"
    str=""
    d=checkline2bin(op)
    str=myDict[op][0] + '000' + d
    return str

def jlt(cmd):
    op = "jlt"
    str = ""
    d=checkline2bin(op)

    str = myDict[op][0] + '000' + d
    return str

def  jgt(cmd):
    op = "jgt"
    str = ""
    d=checkline2bin(op)

    str = myDict[op][0] + '000' + d
    return str

def je(cmd):
    op="je"
    str=""
    d=checkline2bin(op)
    str=myDict[op][0] + '000' + d
    return str

def ld(cmd):
    op="ld"
    str=""

    checkline2bin(op)
    dict[word] = checkline2bin(op)
   
    str= myDict[op][0] + myReg[cmd[1]] + dict["Y"]

    return str

def st(cmd):
    op="st"
    str=""
    d=checkline2bin(op)
    cmnd = "st"
    dict[word] = checkline2bin(cmnd)

    str=myDict[op][0]+ myReg[cmd[1]]+ dict["X"]    
    return str

myList = countline()

def checkA1():
    for cmd in myList:
        if cmd[0] == "mul" or cmd[0]=="add" or cmd[0]=="sub" or cmd[0]=="and" or cmd[0]=="or" or cmd[0]=="xor":
            if (len(cmd) != 4):
                return False
            
            r1 = cmd[1]
            r2 = cmd[2]
            r3 = cmd[3]
            
            if((r1 not in myReg.keys() or r1 == "FLAGS") or (r2 not in myReg.keys() or r2 == "FLAGS") or (r3 not in myReg.keys() or r3 == "FLAGS")):
                return False
            return True                

def checkA2():
    for cmd in myList:
        if cmd[0] == "mul" or cmd[0]=="add" or cmd[0]=="sub" or cmd[0]=="and" or cmd[0]=="or" or cmd[0]=="xor":

            if(len(cmd) != 4):
                file.write("Invalid syntax\n")
                
            else:
                r1 = cmd[1]
                r2 = cmd[2]
                r3 = cmd[3]

                if((r1 not in myReg.keys() or r1 == "FLAGS") or (r2 not in myReg.keys() or r2 == "FLAGS") or (r3 not in myReg.keys() or r3 == "FLAGS")):
                    file.write("Invalid register names\n")
                     

def CheckC1():
    for cmd in myList:
        if cmd[0]=="div" or cmd[0]=="not" or cmd[0]=="cmp" or cmd[0]=="mov":
            if(len(cmd) != 3):
                return False
            r1 = cmd[1]
            r2 = cmd[2]
            if((r1 not in myReg.keys() or r1 == "FLAGS") or (r2 not in myReg.keys() or r2 == "FLAGS")):
                return False
            return True
    
def CheckC2():
    for cmd in myList:
        if cmd[0]=="div" or cmd[0]=="not" or cmd[0]=="cmp" or cmd[0]=="mov":
            if(len(cmd) != 3):
                file.write("Invalid syntax\n")
                
            r1 = cmd[1]
            r2 = cmd[2]
            if((r1 not in myReg.keys() or r1 == "FLAGS") or (r2 not in myReg.keys() or r2 == "FLAGS")):
                file.write("Invalid register usage\n")
                
            return True

def CheckB1():
    for cmd in myList:
        if(cmd[0]=="mov" or cmd[0]=="ls" or cmd[0]=="rs"):
            if(len(cmd) != 3):
                return False
            r = cmd[1]
            if(cmd[2][0] != '$'):
                return False

            im = cmd[2][1:]
            if(im.isdigit() == False):
                return False
            im = int(im)
            if((r not in myReg.keys() or r == "FLAGS")):
                return False
            if im not in range (0, 256):
                return False
            return True 


def CheckB2():
    for cmd in myList:
        if(cmd[0]=="mov" or cmd[0]=="ls" or cmd[0]=="rs"):
            if(len(cmd) != 3):
                file.write("Invalid syntax\n")
                return False
            r = cmd[1]
            if(cmd[2][0] != '$'):
                file.write("Invalid syntax\n")
                return False

            im = cmd[2][1:]
            if(im.isdigit() == False):
                file.write("Invalid immediate value\n")
                return False
            im = int(im)
            if((r not in myReg.keys() or r == "FLAGS")):
                file.write("Invalid register names\n")
                return False
            if im not in range (0, 256):
                file.write("Imm value not in range\n")
                return False
            return True        

def CheckMov1():

    for cmd in myList:  
        op = cmd[0]                   # add for later purpose   
        if(cmd[0]=="mov"):  
            if(op not in myDict.keys()):
                return False
        
            if(len(cmd) != 3):
                return False
            
            if(cmd[2][0] == '$'):
                if(((cmd[1] not in myReg.keys() or cmd[1] == "FLAGS"))):
                    return False
                im = cmd[2][1:]
                if(im.isdigit() == False):
                    return False
                im = int(im)
                if(im not in range(0, 256)):
                    return False
                return True
        
            elif(cmd[2] in myReg.keys()):
                if(cmd[1] in myReg.keys() and cmd[1] != "FLAGS"):
                    return True
                return False
        
            else:
                return True

def CheckMov2():

    for cmd in myList:
        if(cmd[0]=="mov"):
            if(len(cmd) != 3):
                file.write("Invalid syntax\n")

            if(cmd[-1][0] == '$'):
                if(((cmd[1] not in myReg.keys() or cmd[1] == "FLAGS"))):
                    file.write(cmd[1] + " cannot be used as a Register\n")
                    
                im = cmd[2][1:]
                if(im.isdigit() == False):
                    file.write("Invalid immediate value\n")
                    
                im = int(im)
                if(im not in range(0, 256)):
                    file.write("Imm value not in range\n")
                    
                return True
    
            elif(cmd[2] in myReg.keys()):
                if(cmd[1] in myReg.keys() and cmd[1] != "FLAGS"):
                    
                    file.write("Invalid register\n")
                
        
            else:
                file.write("Invalid syntax\n")
                



def CheckD1():
    for cmd in myList:
        if cmd[0]=="ld" or cmd[0]=="st" :
            if(len(cmd) != 3):

                return False
            r = cmd[1]
            
            if((r not in myReg.keys() or r == "FLAGS")):
                return False

            return True



def CheckD2():
    for cmd in myList:
        if cmd[0]=="ld" or cmd[0]=="st" :
            if(len(cmd) != 3):
                file.write("Invalid syntax\n")
                
            r = cmd[1]
            
            if((r not in myReg.keys() or r == "FLAGS")):
                file.write("Invalid register names\n")
                
            return True


def CheckE1():
    for cmd in myList:
        if(cmd[0]== "jmp" or cmd[0]== "jlt" or cmd[0]== "je" or cmd[0]== "jgt"):
            if(len(cmd) != 2):
                return False
            return True

def CheckE2():
    for cmd in myList:
        if(cmd[0]== "jmp" or cmd[0]== "jlt" or cmd[0]== "je" or cmd[0]== "jgt"):
            if(len(cmd) != 2):
                file.write("Invalid syntax\n")
            return True
          
def main():
    for x in myList:
        if x[0]!="hlt":
            if x[0] == "add":
                if checkA1()==False:
                    checkA2()
                else:
                    a = add(x)
                    file.write(a+"\n")
            if x[0] == "sub":
                if checkA1()==False:
                    checkA2()
                else:
                    a = sub(x)
                    file.write(a+"\n")
            if x[0] == "mul":
                if checkA1()==False:
                    checkA2()
                else:
                    a = mul(x)
                    file.write(a+"\n")
            if x[0] == "div":
                if CheckC1()==False:
                    CheckC2()
                else:
                    a = div(x)
                    file.write(a+"\n")
            if x[0] == "mov":
                if(x[-1][0]=="$"):              
                    if CheckMov1()==False:
                        CheckMov2()
                    else:
                        a=mov(x)
                        file.write(a+"\n")   
                elif(x[-1] in myReg.keys()):
                    if CheckMov1()==False:
                        CheckMov2()
                    else:
                        a=mov(x)
                        file.write(a+"\n")
                else:
                    file.write("Invalid syntax\n")

            if x[0] == "ld":
                if CheckD1()==False:
                    CheckD2()
                else:
                    a = ld(x)
                    file.write(a+"\n")
            if x[0] == "st":
                if CheckD1()==False:
                    CheckD2()
                else:
                    a = st(x)
                    file.write(a+"\n")
                
            if x[0] == "cmp":
                if CheckC1()==False:
                    CheckC2()
                else:
                    a = cmp(x)
                    file.write(a+"\n")
            if x[0] == "jmp":
                if CheckE1()==False:
                    CheckE2()
                else:
                    string=""
                    for i in x:
                        string=string+i+" "
                    a=jmp(string)
                    file.write(a+"\n")
            if x[0] == "jlt":
                if CheckE1()==False:
                    CheckE2()
                else:
                    string=""
                    for i in x:
                        string=string+i+" "
                    a=jlt(string)
                    file.write(a+"\n")
            if x[0] == "jgt":
                if CheckE1()==False:
                    CheckE2()
                else:
                    string=""
                    for i in x:
                        string=string+i+" "
                    a=jgt(string)
                    file.write(a+"\n")
            if x[0] == "je":
                if CheckE1()==False:
                    CheckE2()
                else:
                    string=""
                    for i in x:
                        string=string+i+" "
                    a=je(string)
                    file.write(a+"\n")
            if x[0] == "not":
                if CheckC1()==False:
                    CheckC2()
                else:
                    a = Not(x)
                    file.write(a+"\n")
            if x[0] == "xor":
                if checkA1()==False:
                    checkA2()
                else:
                    a = xor(x)
                    file.write(a+"\n")
            if x[0] == "or":
                if checkA1()==False:
                    checkA2()
                else:
                    a = OR(x)
                    file.write(a+"\n")
            if x[0] == "and":
                if checkA1()==False:
                    checkA2()
                else:
                    a = And(x)
                    file.write(a+"\n")
            if x[0] == "ls":
                if CheckB1()==False:
                    CheckB2()
                else:
                    a = ls(x)
                    file.write(a+"\n")
            if x[0] == "rs":
                if CheckB1()==False:
                    CheckB2()
                else:
                    a = rs(x)
                    file.write(a+"\n")
        else:
            a = hlt()
            file.write(a+"\n")
            break

main()



import os
#-------------------------------------
def is_number(s):
    try:
        float(s).is_integer()
        return True
    except ValueError:
        pass
#-------------------------------------
def get_a_int(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    if len(readline) == 2:
                        data0=readline[0].strip('\t\n\r') 
                        data1=readline[1].strip('\t\n\r')
                        if data0 == str(strchain):
                            if is_number(data1):
                                finalvalue=int(data1)
                                return finalvalue
                            else:
                                print('%s is not a number' %(strchain))
                                return False
        bilfile.close()
    print('%s is not specified.' %(strchain))
    return False
#-------------------------------------
def get_str_list(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    data0=readline[0].strip('\t\n\r') 
                    if data0 == str(strchain):
                        del readline[0]
                        data1=[str(item) for item in readline]
                        finalvalue=data1
        bilfile.close()
    return finalvalue
#-------------------------------------
def get_a_float(strchain):
    if os.path.isfile('JAM.inp'):
        bilfile=open('JAM.inp',"r")
        for line in bilfile:
            line=line.strip(' \t\n\r')
            if len(line.strip()) != 0 :
                li = line.lstrip()
                if not li.startswith("#"):
                    readline=line.split()
                    if len(readline) == 2:
                        data0=readline[0].strip('\t\n\r') 
                        data1=readline[1].strip('\t\n\r')
                        if data0 == str(strchain):
                            if is_number(data1):
                                finalvalue=float(data1)
                                return finalvalue
                            else:
                                print('%s is not a number' %(strchain))
                                return False
        bilfile.close()
    print('%s is not specified.' %(strchain))
    return False
#-------------------------------------

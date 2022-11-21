import numpy as np
#-------------------------------------
def split(word):
    return [char for char in word]
#-------------------------------------
def cambio_de_signo(a):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            if ichar[1] != '0':
                if ichar[0] == '+': a[i,j]='-'+ichar[1]
                if ichar[0] == '-': a[i,j]='+'+ichar[1]
    return a
#-------------------------------------
def conv2pseudocanonic(a):
    if a[0,0]=='+0':
        a1=np.copy(a)
        return a1
    else:
        a2=np.array(a[:,[1, 2, 0]])
        if a2[0,0]=='+0':
            return a2
        else:
            a3=np.array(a[:,[2, 0, 1]])
            return a3
#-------------------------------------
#a,b IN PSEUDO-CANONIC FORM
def ask_equivalents1(a,b,optionx):
    b1=np.copy(b)
    b4=np.array(b[:,[0, 2, 1]])
    for bi in [b1,b4]:
        if np.array_equal(a,bi): return True
    return False
#-------------------------------------
#a,b IN PSEUDO-CANONIC FORM
def ask_equivalents2(a,b,optionx):
    b0=np.copy(b)
    b1=np.flipud(b0)
    b1=conv2pseudocanonic(b1)
    b4=np.array(b1[:,[0, 2, 1]])
    if optionx in [3,4,6]:
        b1=cambio_de_signo(b1)
        b4=cambio_de_signo(b4)
    for bi in [b1,b4]:
        if np.array_equal(a,bi):
            return True
    return False
#-------------------------------------
def disc_equivalents(stackinglist,optionx,eqnum):
    repetidos,norepetidos=[],[0]
    for i in range(1,len(stackinglist)):
        a=stackinglist[i]
        ic=True
        for j in norepetidos:
            b=stackinglist[j]
            ans=ask_equivalents1(a,b,optionx) if eqnum==1 else ask_equivalents2(a,b,optionx)
            if ans:
                repetidos.append(i)
                ic=False
                break
        if ic: norepetidos.append(i)
    noreparraylist=[]
    for i in norepetidos:
        noreparraylist.append(stackinglist[i])  
    return noreparraylist
#-------------------------------------
def nparray2chain(a):
    lista=[''.join(j for j in a[:,i]) for i in range(3)]
    chain='/'.join(k for k in lista)
    return chain
#-------------------------------------
def chain2nparray(largechain):
    chain=largechain.split('/')
    wyckoff=[]
    for ic in chain:
        s1=split(ic)
        s2=[s1[x]+s1[x+1] for x in range(0, len(s1),2)]
        wyckoff.append(s2)
    nparray=np.array(wyckoff)
    nparray=nparray.transpose()
    return nparray
#-------------------------------------

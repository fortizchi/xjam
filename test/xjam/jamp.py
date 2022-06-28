#-------------------------------------
def split(word):
    return [char for char in word]
#-------------------------------------
def allatomsx(a,atom_list):
    cj,ck=0,0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            if   ichar[1] == 'j': cj=cj+1
            elif ichar[1] == 'k': ck=ck+1
    allatoms=list(zip(atom_list,[cj,ck]))
    return allatoms
#-------------------------------------
def poscardata(a,zdlist,zlattice,buckling):
    listaxyz=[]
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            ichar=split(a[i,j])
            signo,letra=ichar[0],ichar[1]
            if letra != '0':
                if j==0: xd,yd=0.0000000000,0.0000000000
                if j==1: xd,yd=0.3333333333,0.6666666667
                if j==2: xd,yd=0.6666666667,0.3333333333
                if signo=='-': zd=zdlist[i]-(buckling/zlattice)
                if signo=='+': zd=zdlist[i]+(buckling/zlattice)
                if   letra == 'j': zi=0
                elif letra == 'k': zi=1
                listaxyz.append([xd, yd, zd, zi])
    listaxdydzd = sorted(listaxyz, key=lambda x: int(x[3]))
    return listaxdydzd
#-------------------------------------
def build_poscarx(a,inamex,filename,z_vacuum,num_layers,d,latticep,atom_list,buckling,flag='w'):
    zlattice=(z_vacuum+float(num_layers-1)*d)
    zmax = (zlattice+float(num_layers-1)*d)/2.0
    zdlist=[]
    for ii in range(num_layers):
        zc=zmax-float(ii)*d
        zd=zc/zlattice
        zdlist.append(zd)
    fopen = open(filename,flag)
    print("%s" %(inamex), file=fopen)
    print("%f" %(latticep), file=fopen)
    print("0.500000000  -0.866025403  0.000000000", file=fopen)
    print("0.500000000   0.866025403  0.000000000", file=fopen)
    print("0.000000000   0.000000000  %11.9f" %(zlattice/latticep), file=fopen)
    allatoms=allatomsx(a,atom_list)
    if allatoms[0][1]==0:
        print(allatoms[1][0], file=fopen)
        print(allatoms[1][1], file=fopen)

    if len(allatoms)==2:
        if allatoms[1][1]==0:
            print(allatoms[0][0], file=fopen)
            print(allatoms[0][1], file=fopen)

    else:
        print(' '.join([str(item[0]) for item in allatoms]), file=fopen)
        print(' '.join([str(item[1]) for item in allatoms]), file=fopen)
    print("Direct", file=fopen)
    listaxyz=poscardata(a,zdlist,zlattice,buckling)
    for ixyz in listaxyz:
        xd, yd, zd, si=ixyz[0],ixyz[1],ixyz[2],atom_list[ixyz[3]]
        print("%12.10f %12.10f %12.10f !%s" %(xd, yd, zd, si), file=fopen)
    fopen.close()
#-------------------------------------

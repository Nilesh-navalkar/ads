c=[0,0,0,0,0,0,0,0]

def increment(c):
    if c[-1]==0:
        c[-1]=1
    else:
        j=-1
        while c[j]!=0:
            c[j]=0
            j=j-1
        c[j]=1


increment(c)
increment(c)
increment(c)
increment(c)
print(c)

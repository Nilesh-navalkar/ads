d={0:0,1:0,2:0,3:0,4:0,5:0,6:0}

def h1(e):
    return (2*e+1)%7

def h2(e):
    return (5*e+3)%7

def h3(e):
    return (9*e+6)%7

def search(e):
    a=d[h1(e)]
    b=d[h2(e)]
    c=d[h3(e)]
    print("hash values are : ",(h1(e),h2(e),h3(e)))
    print("the bloom filter values at these hashes are : ",(a,b,c))
    if a==1 and b==1 and c==1:
        print("ALREADY EXISTS\n")
    else:
        d[h1(e)]=1
        d[h2(e)]=1
        d[h3(e)]=1
        print("INSERTED\n")

choice=0
while True:
    if choice==0:
        e=int(input("enter element to insert : "))
        search(e)
        choice=-1
    elif choice==-1:
        print("******************* 0=search and insert\t 1=exit\t 2=print************************")
        choice=int(input("enter choice : "))
    elif choice==1:
        break
    elif choice==2:
        print(d)
        choice=-1


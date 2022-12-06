d1={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
d2={0:0,1:0,2:0,3:0,4:0,5:0,6:0}
d3={0:0,1:0,2:0,3:0,4:0,5:0,6:0}

def h1(e):
    return (2*e+1)%7

def h2(e):
    return (5*e+3)%7

def h3(e):
    return (9*e+6)%7

def insert(e):
    print("hash values are : ",(h1(e),h2(e),h3(e)))
    try:
        d1[h1(e)]=d1[h1(e)]+1
    except:
        d1[h1(e)]=1
    try:
        d2[h2(e)]=d2[h2(e)]+1
    except:
        d2[h2(e)]=1
    try:
        d3[h3(e)]=d3[h3(e)]+1
    except:
        d3[h3(e)]=1
    print("INSERTED\n")

def search(e):
    a=d1[h1(e)]
    b=d2[h2(e)]
    c=d3[h3(e)]
    print("hash values are : ",(h1(e),h2(e),h3(e)))
    print("the values in cms are : ",(a,b,c))
    print("count of ",e," is  : ", min([a,b,c]))

choice=0
while True:
    if choice==0:
        e=int(input("enter element to insert : "))
        insert(e)
        choice=-1
    elif choice==-1:
        print("******************* 0=insert\t3=count\t 1=exit\t 2=print************************")
        choice=int(input("enter choice : "))
    elif choice==3:
        e=int(input("enter element to count : "))
        search(e)
        choice=-1
    elif choice==1:
        break
    elif choice==2:
        print(d1)
        print(d2)
        print(d3)
        choice=-1


a=[None]
tail=0

def addele(e):
    global a,tail
    if (len(a)-1)<tail:
        temp=[]
        for i in range(0,2*len(a)):
            temp.append(None)
        for i in range(0,len(a)):
            temp[i]=a[i]
        a=temp
    
    a[tail]=e
    tail=tail+1

choice=1
while True:
    if choice==1:
        e=int(input("enter element to insert : "))
        addele(e)
        choice=-1
    elif choice==2:
        print(a)
        choice=-1
    elif choice==3:
        break
    elif choice==-1:
        print("******1==insert\t 2==print\t 3==exit *****")
        choice=int(input("enter choice : "))
    

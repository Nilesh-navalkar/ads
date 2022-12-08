stack=[]
def push(ele):
    stack.append(ele)

def pop():
    if len(stack)==0:
        print("underflow")
    else:
        print(stack.pop())

def multipop(k):
    for i in range(0,k):
        pop()

choice=1
while True:
    if choice==1:
        print("enter element to push : ")
        ele=int(input())
        push(ele)
        choice=-1
    elif choice==2:
        pop()
        choice=-1  
    elif choice==3:
        print("enter k : ")
        k=int(input())
        multipop(k)
        choice=-1
    elif choice==4:
        print(stack)
        choice=-1
    elif choice==0:
        break
    elif choice==-1:
        print("***********0==exit\t 1==push\t 2==pop\t 3==multipop\t 4==print stack**********")
        choice=int(input("enter choice : "))

    

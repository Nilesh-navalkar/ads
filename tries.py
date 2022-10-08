class node:
    def __init__(self,char):
        self.char=char
        self.end=0
        self.pointer=[]
        for i in range(0,26):
            self.pointer.append(-1)

root=node(0)
#print(ord("b")-ord("a"))
def printnode(root):
    current=root
    n=0
    while current.end!=1:
        for i in current.pointer:
            if(i!=-1):
                print(i.char)
                current=current.pointer[current.pointer.index(i)]
 

def insert(root,data):
    current=root
    k=0
    for i in data:
        idx=ord(i)-ord("a")
        if(current.pointer[idx]==-1):
            n=node(i)
            if(k==len(data)-1):
                n.end=1
            current.pointer[idx]=n
            #print(current.pointer)
            current=current.pointer[idx]
        else:
            current=current.pointer[idx]
            if(k==len(data)-1):
                current.end=1
        
        k=k+1

def searchnode(root,data):
    current=root
    for i in data:
        idx=ord(i)-ord("a")
        if(current.pointer[idx]==-1):
            print(data," doesent exist in trie")
            return
        elif(current.pointer[idx].char==i):
            #print("found ",i)
            current=current.pointer[idx]

    if(current.end==1):
        print(data," exists in trie")
    else:
        print(data," doesent exist in trie")

def delnode(root,data):
    current=root
    for i in data:
        idx=ord(i)-ord("a")
        if(current.pointer[idx]==-1):
            print(data," doesent exist in trie cant delete")
            return
        elif(current.pointer[idx].char==i):
            #print("found ",i)
            current=current.pointer[idx]

    if(current.end==1):
        current.end=0
        print("node deleted")
    else:
        print(data," doesent exist in trie cant delete")

    

loop=True
choice=1
print("\n1==insert\t2==search\t3==delete\t4==exit\n")
while(loop):
    if choice==1:
        ele=input("enter the node to insert : ")
        insert(root,ele)
        choice=-1
    elif choice==2:
        ele=input("enter the node to search : ")
        searchnode(root,ele)
        choice=-1
    elif choice==3:
        ele=input("enter the node to delete : ")
        delnode(root,ele)
        choice=-1
    elif choice==-1:
        print("\n1==insert\t2==search\t3==delete\t4==exit")
        choice=int(input("enter your choice : "))
    elif choice==4:
        loop=False


import numpy
import random as r

cost=0
s=[]
ele=1
k=0
def push(ele):
    global cost,k
    s.append(ele)
    cost=cost+1
    k=k+1

def pop():
    global cost,k
    if len(s)!=0:
        print(s[len(s)-1])
        del s[len(s)-1]
        cost=cost+1
        k=k+1
    else:
        print("underflow")


def multipop(no):
    global cost
    n=min(no,len(s))
    for i in range(0,n):
        pop()

#k=int(input("enter no of operations : "))
'''
k=5
operations=numpy.random.uniform(0,3,k)
o=operations.astype(int)
'''
o=[0,0,0,1,1,0,2,0,2,0,0,2,0,1]

for i in o:
    if i==0:
        push(ele)
    elif i==1:
        pop()
    elif i==2:
        x=r.randrange(1,10)
        x=3
        print("muptipopin ",x," times")
        multipop(x)
print("0: push \t1: pop\t2: multipop")
print("operations : ", o)
print("aggregate amortized cost : ",cost/len(o))



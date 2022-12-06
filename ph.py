import random

m=int(input("enter number of keys : "))
m=10
p=7
keys=[]
collision_frequency={}
d={}

def gethash(a,b,p,e,m):
    #print(a,b,p,e,m)
    #print(((a*e+b)%p)%m)
    return ((a*e+b)%p)%m

print("enter the keys : ")
for i in range(0,m):
    e=int(input())
    keys.append(e)

for i in keys:
    h=gethash(5,6,p,i,m)
    try:
        collision_frequency[h]=collision_frequency[h]+1
    except:
        collision_frequency[h]=1
        
print(collision_frequency)
for i in collision_frequency.keys():
    M=collision_frequency[i]

    size=M*M
    l=[]
    for k in range(0,size+3):
        l.append(None)
    if size==1:
        a=0
        b=0
    else:
        a=random.randint(1,20)
        b=random.randint(1,20)
    l[0]=a
    l[1]=b
    l[2]=M
    d[i]=l
print(d)
for i in keys:
    h=gethash(5,6,p,i,m)
    a=d[h]
    h1=gethash(a[0],a[1],p,i,a[2]*a[2])
    #print(i,h,h1,a[0],a[1],a[2])
    #print(h1)
    d[h][h1+3]=i

print(d)






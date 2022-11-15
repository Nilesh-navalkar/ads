#segment tree
class node:
    def __init__(self,r):
        self.r=r
        self.left=None
        self.right=None
        self.val=False


def maketree(arr,root):
    if root.r[0]!=root.r[1]:
        #print(root.r[0],root.r[1])
        root.left=node((root.r[0],(root.r[0]+root.r[1])//2))
        root.right=node(((root.r[0]+root.r[1])//2+1,root.r[1]))
        maketree(arr,root.left)
        maketree(arr,root.right)
    elif(root.r[0]==root.r[1]):
        root.val=arr[root.r[0]]
        #print(root.r[0],root.r[1],root.val)

def enum(root):
    if root.val:
        a=0
    elif root.left.val and root.right.val:
        #print(root.r[0],root.r[1],root.val,root.left.val, root.right.val)
        root.val=root.left.val+root.right.val
    elif not root.val:
        #print(root.r[0],root.r[1],root.val,root.left.val, root.right.val)
        enum(root.left)
        enum(root.right)
        

def inorder(root):
    if root:
        inorder(root.left)
        print((root.r),root.val)
        inorder(root.right)

def query(interval,root):
    l=interval[0]
    h=interval[1]
    if l<=root.r[0] and h>=root.r[1]:
        return root.val
    elif (l>root.r[1] and h>root.r[1]) or (l<root.r[0] and h<root.r[0]):
        return 0
    else:
        return query(interval,root.left) + query(interval,root.right)

    

#arr=[1,3,5,7,9,11]
arr=[]
n=int(input("enter length of array : "))
for i in range(0,n):
    e=int(input())
    arr.append(e)

root=node((0,len(arr)-1))
maketree(arr,root)
while not root.val:
    enum(root)

print("inorder : ")
inorder(root)
print("queries")
while True:
    l=int(input("enter lower : "))
    h=int(input("enter high :"))
    print(query((l,h),root))
    c=int(input("0==exit 1==continue"))
    if c==0:
        break
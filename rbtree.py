import copy

class node:
    def __init__(self,val):
        self.val=val
        self.color="r"
        self.left=None
        self.right=None

def insert(tree,val):
    if(tree==None):  #root
        return node(val)
    elif(tree.val>val):
        tree.left=insert(tree.left,val)
    else:
        tree.right=insert(tree.right,val)

    return tree


def lr(g,p):
    temp=p.left
    p.left=g
    g.right=temp
    return p

def rr():
    pass


def checkinsert(tree):
    if tree is None:
        return
    if(tree.right.color==tree.right.right.color=="r"):
        if(tree.left.color=="r"):
            tree.left.color=tree.right.color="b"
            if(tree.color=="r"):
                tree.color="b"
            else:
                tree.color="r"
        else:
            tree=lr(tree,tree.right)
            tree.color="b"
            tree.left.color=tree.right.color="r"
            pass
    elif(tree.right.color==tree.right.left.color=="r"):       
        if(tree.left.color=="r"):
            tree.left.color=tree.right.color="b"
            if(tree.color=="r"):
                tree.color="b"
            else:
                tree.color="r"
        else:
            pass
    elif(tree.left.color==tree.left.left.color=="r"):
        if(tree.right.color=="r"):
            tree.left.color=tree.right.color="b"
            if(tree.color=="r"):
                tree.color="b"
            else:
                tree.color="r"
        else:
            pass
    elif(tree.left.color==tree.left.right.color=="r"):
        if(tree.right.color=="r"):
            tree.left.color=tree.right.color="b"
            if(tree.color=="r"):
                tree.color="b"
            else:
                tree.color="r"
        else:
            pass
    checkinsert(tree.right)
    checkinsert(tree.left)

def insertrb(root,val):
    insert(root,val)
    checkinsert(root)

def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)

root=node(5)
root.color="b"
insert(root,8)
insert(root,6)
insert(root,9)
insert(root,3)
insert(root,2)
insert(root,4)
inorder(root)
root=lr(root,root.right)

print(root.val,root.left.val,root.right.val)
inorder(root)

def delete(tree,val):
    pass

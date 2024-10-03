class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.value<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
        
def find_height(root):
    if root is None:
        return -1
    if root is not None:
        left=find_height(root.left)
        right=find_height(root.right)
    return max(left,right)+1

root=Node(10)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)

inorder(root)

height=find_height(root)
print(height)

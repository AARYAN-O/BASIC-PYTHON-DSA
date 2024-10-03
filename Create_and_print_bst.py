class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    
def insert(root,key):
    if root is None:
        return Node(key)
    # create new Node if root is None
    else:
        if root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
    
def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
    
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")

root=Node(10)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)

print("inorder traversal")
inorder(root)
print()

print("post order traversal")
postorder(root)
print()

print("preorder traversal")
preorder(root)
print()


# What is the difference between binary tree and bst ?
# The difference is that in binary tree the order of arrangement can be anything 
# In bst order of arrangement is specific meaning that the left node should always be lesser than the right node value.
# Note : inorder traversal is always sorted.
    

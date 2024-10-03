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

def height_of_left_tree(root):
    if root is None:
        return -1
    else:
        left=height_of_left_tree(root.left)
    return left+1 

def height_of_right_tree(root):
    if root is None:
        return -1
    else:
        right=height_of_right_tree(root.right)
    return right+1 

def balance_decider(root):
    if abs(height_of_left_tree(root)-height_of_right_tree(root))==1:
        print("Tree is balanced")
    else:
        print("tree is unbalanced")

root=Node(10)
root=insert(root,20)
root=insert(root,30)
root=insert(root,40)

inorder(root)

print(height_of_right_tree(root))
print(height_of_left_tree(root))

balance_decider(root)


    
    
    
    

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None 
    
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def printList(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    
obj=LinkedList()
obj.insertAtBeginning(12)
obj.insertAtBeginning(14)
obj.printList()

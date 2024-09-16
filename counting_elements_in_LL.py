class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class LinkedList:
    def __init__(self):
        self.head=None 
        
    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while last.next is not None:
                last=last.next
            last.next=new_node
            
    def countList(self):
        current=self.head
        cnt=0
        while current is not None:
            cnt=cnt+1
            current=current.next
        print("The count of the list is "+str(cnt))
        
obj=LinkedList()
obj.insertAtEnd(12)
obj.insertAtEnd(14)
obj.insertAtEnd(16)
obj.insertAtEnd(18)
obj.countList()
        

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            new_node.next=last
            self.head=new_node
    
    def countLL(self):
        current=self.head
        cnt=0
        while current:
            cnt=cnt+1
            current=current.next
        return cnt
            
        
    def middle_of_LL(self):
        current=self.head
        cnting=0
        if self.countLL()%2==0:
            indx=self.countLL()//2
        else:
            indx=(self.countLL()//2)
        while current:
            if cnting==indx:
                return current.data
            current=current.next
            cnting=cnting+1 

        
obj=LinkedList()
obj.insertAtBeginning(12)
obj.insertAtBeginning(14)
obj.insertAtBeginning(16)
obj.insertAtBeginning(18)
# obj.insertAtBeginning(20)
print(obj.middle_of_LL())
        

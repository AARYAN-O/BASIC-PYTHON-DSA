class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None :
            self.head=new_node
            return
        
        last=self.head
        
        while last.next is not None:
            last=last.next
        last.next=new_node
        
        
    def insertAfterData(self,data,prev_data):
        new_node=Node(prev_data)
        current=self.head
        # print("current head"+str(current.data))
        while current.data!=prev_data:
            current=current.next
        current.next=new_node
    
    def printList(self):
        current=self.head
        if current is None:
            print("List is empty")
        else:
            while current is not None:
                print(current.data)
                current=current.next

obj=LinkedList()
obj.insertAtEnd(12)
obj.insertAtEnd(14)
# obj.printList()
obj.insertAfterData(16,12)
obj.printList()
            
    

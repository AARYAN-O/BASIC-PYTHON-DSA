class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
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
    def reverse_LL(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
    def printList(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        
obj=LinkedList()
obj.insertAtEnd(12)
obj.insertAtEnd(14)
obj.insertAtEnd(16)
obj.insertAtEnd(18)
obj.printList()
print("reversed Linked List")
obj.reverse_LL()
obj.printList()

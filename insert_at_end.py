class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        
    def print_list(self):
        current=self.head
        if current is None:
            print("list is empty")
        else:
            while current:
                print(current.data)
                current=current.next
        
obj=LinkedList()
obj.insert_at_end(12)
obj.insert_at_end(14)
obj.insert_at_end(16)
obj.print_list()

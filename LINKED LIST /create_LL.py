class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        # agar head present nahi hai toh
        if not self.head:
            self.head=new_node
            return
        # agar head present hai toh maan lo ki last node hi head node hai
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    
    def print_list(self):
        current_node=self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        
list=LinkedList()
list.append(1)
list.append(2)
list.print_list()

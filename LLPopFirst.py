class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:   
            self.head = new_node
            self.tail = new_node 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
   
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
my_ll = LinkedList(1)
my_ll.append(2)
my_ll.print_list()

print(my_ll.pop_first()) #pops node 1
print(my_ll.pop_first()) #pops node 2
print(my_ll.pop_first()) #pops none




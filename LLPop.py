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

    def pop(self):
        if self.head is None:    #to check if ll is empty 
            return None
        pre = self.head
        temp = self.head
        while(temp.next is not None):    #if ll has 2 or more elements
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:      #if only one node is in ll
            self.head = None
            self.tail == None
        return temp   #or return temp.value
        





my_linked_list = LinkedList(3)
my_linked_list.append(4)

print(my_linked_list.pop())  # item return 4 node

print(my_linked_list.pop())  # item returns 3 node

print(my_linked_list.pop())  # item returns none





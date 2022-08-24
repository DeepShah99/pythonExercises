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

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        pre = temp.next
        temp.next = temp.next.next 
        pre.next = None
        self.length -= 1
        return pre
        






my_linked_list = LinkedList(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
print(my_linked_list.remove(2))
my_linked_list.print_list()



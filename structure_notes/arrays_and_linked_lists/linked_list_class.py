class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

class LinkedList():
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
    

    def append(self, value):
        '''Adds a value to the end of the list: O(n)
        '''
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    
    def prepend(self, value):
        ''' Prepend a value to the beginning of the list: O(1)
        '''
        if self.head is None:
            self.head = Node(value)
            return
        
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
    
    
    def search(self, value):
        '''Search the linked list for a node with the requested value and
            return the node.'''
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")
    
    
    def remove(self, value):
        '''Delete the first node with the desired data.'''
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")
    
    
    def pop(self):
        '''Return the first node's value and remove it from the list.'''
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value


    def insert(self, value, pos):
        '''Insert value at pos position in the list. If pos is larger than the 
        length of the list, append to the end of the list.'''
        # If the list is empty 
        if self.head is None:
            self.head = Node(value)
            return
            
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)
        

    def size(self):
        '''Return the size or length of the linked list.'''
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    
    def to_list(self):
        '''Converts a linked list back into a Python list.
        '''
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list
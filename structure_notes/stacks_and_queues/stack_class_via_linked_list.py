class Node():
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack():
    def __init__(self, node=None):
        self.head = node
        self.item_count = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.item_count += 1
        
        
    def pop(self):
        if self.is_empty():
            return None

        pop_item = self.head.value
        self.head = self.head.next
        self.item_count -= 1
        return pop_item
    
    def size(self):
        return self.item_count
    
    def is_empty(self):
        return self.item_count == 0
    
    def top(self):
        if self.head is None:
            return None
        return self.head.value

def print_stack(stack):
    itr = iter(stack)
    for _ in range(stack.size()):
        print(next(itr))
    

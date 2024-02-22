from linked_list_class import Node


class SortedLinkedList:
    '''Given a stream of random integers, create a linked list that is always
    sorted from ascending order (lowest to highest). What's the computational
    complexity of adding an element in this way?

    Computational complexity is  O(N) where  N is the current length of 
    the linked list.
    '''
    
    def __init__(self):
        self.head = None
    
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return
        
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        
        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next
            
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        
        return None

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)
    
    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next
    
    return sorted_array

'''Computational complexity is  O(N2) where N is the length of the integer 
array. One insert is  O(M) where M is the length of the existing linked 
list. As the list grows, the time complexity of inserting grows. 
It's something like  1+2+3+4+⋯+N.

Sorting algorithms such as quicksort and mergesort are  NlogN, 
so this algorithm is slower.
'''

##############################################################################
# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")


print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")

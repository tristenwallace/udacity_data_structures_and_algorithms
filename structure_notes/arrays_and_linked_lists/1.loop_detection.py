from linked_list_class import Node, LinkedList

def has_loop(linked_list):
    '''
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    '''
    
    if linked_list.head is None:
        return False
    if linked_list.head.next is None:
        return False
    
    start = linked_list.head 
    slow = start
    fast = start.next
    

    while slow != fast:
        slow = slow.next
        if fast.next.next is None:
            return False
        fast = fast.next.next
    return True


##############################################################################
#TEST

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ('Pass' if has_loop(list_with_loop) else 'Fail')                  # Pass
print ('Pass' if has_loop(LinkedList([-4, 7, 2, 5, -1])) else 'Fail')   # Fail
print ('Pass' if has_loop(LinkedList([1])) else 'Fail')                 # Fail
print ('Pass' if has_loop(small_loop) else 'Fail')                      # Pass
print ('Pass' if has_loop(LinkedList([])) else 'Fail')                  # Fail

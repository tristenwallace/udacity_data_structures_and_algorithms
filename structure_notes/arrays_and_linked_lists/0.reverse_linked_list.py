from linked_list_class import Node, LinkedList

def reverse(linked_list):
    '''
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    '''
    new_list = LinkedList()
    
    prev_node = None

    '''
    A simple idea - Pick a node from the original linked list traversing form the beginning, and 
    prepend it to the new linked list. 
    We have to use a loop to iterate over the nodes of original linked list
    '''
    # In this 'for' loop, the 'value' is just a variable whose value will be updated in each iteration
    for value in linked_list:
        # create a new node
        new_node = Node(value)
        
        # Make the new_node.next point to the 
        # node created in previous iteration
        new_node.next = prev_node 
        
        # This is the last statement of the loop
        # Mark the current new node as the 'prev_node' for next iteration
        prev_node = new_node
    
    # Update the new_list.head to point to the final node that came out of the loop
    new_list.head = prev_node
    
    return new_list


##############################################################################
#TEST

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
### Given a linked list, swap the two nodes present at position i and j, 
# assuming 0 <= i <= j. The positions are based on 0-based indexing.

from linked_list_class import Node, LinkedList

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped
"""
def swap_nodes(head, position_one, position_two):

    # If both the indices are same
    if position_one == position_two:
        return head
    
    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head 
    new_head = None

    # LOOP - find out previous and current node at both the positions (indices)
    while current_node is not None:
        
        # Position_one cannot be equal to position_two, 
        # so either one of them might be equal to the current_index
        if current_index == position_one:
            one_current = current_node
        
        elif current_index == position_two:
            two_current = current_node
            break

        # If neither of the position_one or position_two are equal to the current_index
        if one_current is None:
            one_previous = current_node
        
        two_previous = current_node
        
        # increment both the current_index and current_node
        current_node = current_node.next         
        current_index += 1
        

    # Loop ends
    
    
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: one_current & two_current to be swapped, 
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    
    # if the node at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends
    
    return new_head

##############################################################################

def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")
        
#test 1
arr = [3, 4, 5, 2, 6, 1, 9]
linked_list = LinkedList(arr)
head = linked_list.head
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

#test 2
arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2 
right_index = 4
linked_list = LinkedList(arr)
head = linked_list.head
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

#test 3
arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
linked_list = LinkedList(arr)
head = linked_list.head
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)
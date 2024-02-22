from linked_list_class import Node, LinkedList

'''
The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
For this purpose, we will use four helper references, that denotes starting and 
current ending of EVEN and ODD sub-list respectively. 

1. For each Node in the LinkedList, check if its data is even/odd. 
Change the 'next' reference (pointer) of each Node, based on the following rules:
 - First even valued Node will be referenced by head of EVEN sub-list
 - Subsequent even valued Node will be appended to the tail of EVEN sub-list

 - First odd valued Node will be referenced by head of ODD sub-list
 - Subsequent odd valued Node will be appended to the tail of ODD sub-list
 
2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
'''
##############################################################################

def even_after_odd(head):
    
    if head is None:
        return head
    
    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the 'EVEN' sub-list '''
    even_head = None                    
    even_tail = None
    
    ''' `odd_head` and `odd_tail` represents the starting and current ending of the 'ODD' sub-list '''
    odd_head = None
    odd_tail = None
    
    node = head                  # <-- 'current' represents the current Node. 
    
    # Loop untill there are Nodes available in the LinkedList
    while node:                  # <-- 'current' will be updated at the end of each iteration
        
        next_node = node.next    # <-- 'next_node' represents the next Node w.r.t. the current Node
        
        if node.value % 2 == 0:   # <-- current Node is even
            
            # Below 
            if even_head is None:   # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = node     # `even_head` will now point where `current` is already pointing
                even_tail = even_head     
            else:                   # <-- Append the current even node to the tail of EVEN sub-list 
                even_tail.next = node
                even_tail = even_tail.next
        else:
            if odd_head is None:    # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = node
                odd_tail = odd_head
            else:                   # <-- Append the current odd node to the tail of ODD sub-list 
                odd_tail.next = node
                odd_tail = odd_tail.next
        node.next = None
        node = next_node         # <-- Update 'head' Node, for next iteration
    
    if odd_head is None:            # <-- Special case, when there are no odd Nodes 
        return even_head

    odd_tail.next = even_head       # <-- Append the EVEN sub-list to the tail of ODD sub-list
    
    return odd_head

##############################################################################
def print_linked_list(head):
    while head:
        print(head.value, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.value != solution[index] or temp not in node_tracker['nodes']:
                print('Fail')
                return
            temp = temp.next
            index += 1
        print('Pass')            
    except Exception as e:
        print('Fail')



#test 1
arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

linked_list = LinkedList(arr)
head = linked_list.head
test_case = [head, solution]
test_function(test_case)

#test 2
arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

linked_list = LinkedList(arr)
head = linked_list.head
test_case = [head, solution]
test_function(test_case)

#test 3
arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
linked_list = LinkedList(arr)
head = linked_list.head
test_case = [head, solution]
test_function(test_case)
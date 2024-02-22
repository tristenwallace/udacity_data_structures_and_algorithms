### You are given the head of a linked list and two integers, i and j. You 
# have to retain the first i nodes and then delete the next j nodes. Continue
# doing so until the end of the linked list.

from linked_list_class import Node, LinkedList

'''
:param: head - head of linked list
:param: i - first `i` nodes that are to be skipped
:param: j - next `j` nodes that are to be deleted
return - return the updated head of the linked list
'''
'''
The Idea: 
Traverse the Linkedist. Make use of two references - `current` and `previous`.
 - Skip `i-1` nodes. Keep incrementing the `current`. Mark the `i-1`^th node as `previous`. 
 - Delete next `j` nodes. Keep incrementing the `current`.
 - Connect the `previous.next` to the `current`
'''
def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes (means Delete all nodes)
    if i == 0:
        return None
    
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # Helper references
    node = head
    previous = None
    
    # Traverse - Loop untill there are Nodes available in the LinkedList
    while node:
        
        '''skip (i - 1) nodes'''
        for _ in range(i - 1):
            if node is None:
                return head
            node = node.next
        previous = node
        node = node.next
        
        '''delete next j nodes'''
        for _ in range(j):
            if node is None:
                break
            next_node = node.next
            node = next_node
        
        '''Connect the `previous.next` to the `current`''' 
        previous.next = node
    
    # Loop ends
    
    return head

##############################################################################
def print_linked_list(head):
    while head:
        print(head.value, end=' ')
        head = head.next
    print()
    
def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.value != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")
        
#test 1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
linked_list = LinkedList(arr)
head = linked_list.head
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

#test 2
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
linked_list = LinkedList(arr)
head = linked_list.head
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

#test 3
arr = [1, 2, 3, 4, 5]
i = 2
j = 4
linked_list = LinkedList(arr)
head = linked_list.head
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)

#test 4
arr = [1, 2, 3, 4, 5]
i = 2
j = 0
linked_list = LinkedList(arr)
head = linked_list.head
solution = [1, 2, 3, 4, 5]
test_case = [head, i, j, solution]
test_function(test_case)
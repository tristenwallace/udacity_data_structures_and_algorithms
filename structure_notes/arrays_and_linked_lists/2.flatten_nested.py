from linked_list_class import Node, LinkedList

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged

''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head) # <-- self.head is a node for NestedLinkedList

    '''  A recursive function ''' 
    def _flatten(self, node):
        
        # A termination condition
        if node.next is None:
            return merge(node.value, None) # <-- First argument is a simple LinkedList
        
        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next)) # <-- Both arguments are a simple LinkedList each


##############################################################################
#TEST

''' Create a simple LinkedList'''
linked_list = LinkedList([1, 3, 5])

''' Create another simple LinkedList'''
second_linked_list = LinkedList([2, 4])

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList([linked_list, second_linked_list]) # <-- Notice that we are passing a Node made up of a simple LinkedList object

''' Test merge() function'''
merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 3 5
    print(node.value)
    node = node.next
    

''' Test flatten() function'''
# Call the `flatten()` function
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
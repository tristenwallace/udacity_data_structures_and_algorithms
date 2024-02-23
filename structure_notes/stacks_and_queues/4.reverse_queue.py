from queue_via_linked_list import Node, Queue
from stack_class_via_linked_list import Stack

def reverse_queue(queue):
    '''
    Reverese the input queue

    Args:
        queue(queue),str2(string): Queue to be reversed
    Returns:
        queue: Reveresed queue
    '''
    
    # Write reversed queue function
    stack = Stack()
    if queue.size() < 2:
        return queue
    
    while not queue.is_empty():
        stack.push(queue.dequeue())
    
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    
    return queue
    
##############################################################################

def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")
    
test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)


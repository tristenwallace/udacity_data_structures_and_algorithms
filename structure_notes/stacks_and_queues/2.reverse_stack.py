from stack_class_via_linked_list import Node, Stack

def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
        stack(stack): Input stack to be reversed
    Returns:
        stack: Reversed Stack
    """
    new_stack = Stack()
    
    while not stack.is_empty():
        new_stack.push(stack.pop())
    
    return new_stack

##############################################################################

def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)
    
    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")
    
#test 1
test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

#test 2
test_case_2 = [1]
test_function(test_case_2)
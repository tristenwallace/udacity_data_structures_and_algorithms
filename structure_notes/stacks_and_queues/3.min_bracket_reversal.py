# Given an input string consisting of only { and }, figure out the minimum 
# number of reversals required to make the brackets balanced.

from stack_class_via_linked_list import Node, Stack
    
def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
        input_string(string): Strings to be used for bracket reversal calculation
    Returns:
        int: Number of breacket reversals needed
    """
    if len(input_string) % 2 == 1:
        return -1

    stack = Stack()
    count = 0
    for bracket in input_string:
        if stack.is_empty():
            stack.push(bracket)
        else:
            top = stack.top()
            if top != bracket:
                if top == '{':
                    stack.pop()
                    continue
            stack.push(bracket)

    ls = list()
    while not stack.is_empty():
        first = stack.pop()
        second = stack.pop()
        ls.append(first)
        ls.append(second)
        if first == '}' and second == '}':
            count += 1
        elif first == '{' and second == '}':
            count += 2
        elif first == '{' and second == '{':
            count += 1
    return count

##############################################################################
def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")
        
test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]          
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_1)

test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_3)
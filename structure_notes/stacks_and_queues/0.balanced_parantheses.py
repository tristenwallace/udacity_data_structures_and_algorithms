### Take a string as an input and return True if it's parentheses are 
# balanced or False if it is not.

from stack_class_py_methods import Stack

def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    #Intiate stack object
    stack = Stack()
    
    #Interate through equation checking parentheses
    pairs = {')':'(',
            '}':'{',
            ']':'['
            }
        
    print(f'Checking: {equation}')
    for char in equation:
        if char in (set(pairs.keys()) | set(pairs.values())):
            if char in {'(', '{', '['}:
                stack.push(char)
            elif not stack.is_empty():
                if pairs[char] == stack.items[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    
    #Return True if balanced and False if not
    return stack.is_empty()

##############################################################################
#TEST

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
print ("Pass" if not (equation_checker(')')) else "Fail")
print ("Pass" if not (equation_checker('[')) else "Fail")
print ("Pass" if not (equation_checker('(2]')) else "Fail")
### You are given a non-negative number in the form of list elements. For 
# example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the
# number and return the output in the form of a new list.

def add_one(arr):
    '''
    param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    '''
    
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        arr = add_one(arr[:-1]) + [0]
    
    return arr

##############################################################################
# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")      
    
# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
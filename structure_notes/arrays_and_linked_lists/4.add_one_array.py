### You are given a non-negative number in the form of list elements. For 
# example, the number 123 would be provided as arr = [1, 2, 3]. Add one 
# to the number and return the output in the form of a new list.

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    for i, value in enumerate(arr[::-1]):
        if value < 9:
            arr[-(i+1)] += 1
            return arr
        elif i+2 <= len(arr):
            arr[-(i+1)] = 0
            arr[-(i+2)] += 1
        else:
            arr.append(0)
            arr[-(i+2)] = 1
            return arr


##############################################################################

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
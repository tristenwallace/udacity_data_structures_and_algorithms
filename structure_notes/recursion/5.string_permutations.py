def permutations(string):
    '''
    :param: input string
    Return - list of all permutations of the input string
    '''
    
    # output to be returned
    output = list()
    
    # Terminaiton / Base condition
    if len(string) == 1:
        output.append(string)
        return output 
    
    
    else:
        first_char = string[0]
        rest_chars = string[1:]
        
        # Recursive function call
        strings = permutations(rest_chars)
        
        # Iterate over each sub-string available in the list returned from previous call
        for sub_string in strings:
            # place the current character at different indices of the sub-string
            for index in range(len(sub_string)+1):
                # Make use of the sub-string of previous output, to create a new sub-string.
                new_string = sub_string[0:index] + first_char + sub_string[index:]
                output.append(new_string)

    return output
    
##############################################################################
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system

    Returns:
        a list of paths
    """
    filter_list = []
    
    for fileName in os.listdir(path):
        newPath = os.path.join(path, fileName)
        if os.path.isdir(newPath):
            for file in find_files(suffix, newPath):
                filter_list.append(file)
        elif os.path.isfile(newPath) and newPath.endswith(suffix):
            filter_list.append(newPath)
    
    return filter_list

## Test Case 1
'''
SUCCESS:
['2_testdir/subdir1/a.c', '2_testdir/t1.c', '2_testdir/subdir5/a.c', 
'2_testdir/subdir3/subsubdir1/b.c']

'''
src = "2_testdir"
suffix = '.c'
print(find_files(suffix, src))

## Test Case 2
'''
SUCCESS:
['2_testdir/subdir1/a.h', '2_testdir/subdir1/a.c', '2_testdir/t1.h', 
'2_testdir/subdir4/.gitkeep', '2_testdir/t1.c', '2_testdir/subdir2/.gitkeep', 
'2_testdir/subdir5/a.h', '2_testdir/subdir5/a.c', '2_testdir/subdir3/subsubdir1/b.c', 
'2_testdir/subdir3/subsubdir1/b.h']
'''
src = "2_testdir"
suffix = ''
print(find_files(suffix, src))

## Test Case 3
'''
SUCCESS:
['2_testdir/subdir4/.gitkeep', '2_testdir/subdir2/.gitkeep']
'''
src = "2_testdir"
suffix = 'keep'
print(find_files(suffix, src))
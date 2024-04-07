# 2.File Recursion

## Efficiency
The find_files function employs a recursive approach to traverse directory trees, making it adept at handling nested subdirectories of arbitrary depth. This recursion ensures that each directory and file is visited exactly once, leading to a time complexity of O(n), where n is the total number of files and directories in the path. The space complexity is also O(n) due to the recursion stack and the storage of file paths in the filter_list.

## Code Design
The function is designed to recursively traverse through each directory, checking each entry to determine if it's a directory or a file that matches the specified suffix. When a directory is encountered, the function recursively searches within, and when a matching file is found, its path is added to the result list. This design effectively separates the concerns of directory traversal and file filtering.
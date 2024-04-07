# 6.Union & Intersection

## Efficiency
The union and intersection functions both traverse through each element of the input linked lists, resulting in a time complexity of O(n + m) for each function, where n and m are the sizes of the two linked lists. The use of Python sets in both functions to store unique elements ensures that each element is added or checked for existence in constant time, O(1). However, when converting the set back to a linked list in the union and intersection functions, the time complexity is O(k) for k unique elements. Therefore, the overall time complexity remains O(n + m).

Space complexity for both functions is primarily influenced by the size of the sets used to store unique elements and the resulting linked list. In the worst case, where all elements are unique, the space complexity would be O(n + m) due to the storage requirements of the set and the resulting linked list.


## Code Design
The LinkedList and Node classes provide a basic structure for linked list operations, with append and size methods supporting list manipulation and size retrieval, respectively. The union and intersection functions showcase a practical use of sets for collection operations, leveraging their properties for efficient element lookup and uniqueness. The design separates concerns by maintaining linked list operations within the LinkedList class and set operations within the union and intersection functions, adhering to principles of modularity and single responsibility.
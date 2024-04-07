# 4.Active Directory

## Efficiency
The is_user_in_group function employs a recursive depth-first search (DFS) approach to navigate through the group hierarchy. This method ensures that each group and subgroup is visited once, leading to a time complexity of O(n), where n represents the total number of groups and subgroups within the given group hierarchy. In the worst-case scenario, where a user is located at the deepest level or not present, the function will traverse the entire tree. The space complexity is O(h) due to the recursion stack, with h being the height of the group hierarchy, which could be significant in cases of deep nesting.


## Code Design
The design encapsulates group-related data within the Group class, including child groups and users, allowing for clear and modular representation of the group structure. The recursive is_user_in_group function is a straightforward application of DFS, apt for the hierarchical nature of the problem. The choice to check immediate group members before recursive subgroup checks is efficient for cases where the user is found early in the hierarchy.
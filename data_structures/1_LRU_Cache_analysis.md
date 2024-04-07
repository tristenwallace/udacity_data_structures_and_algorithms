# 1.LRU Cache

## Efficiency
Time efficiency is achieved by using a hash table (the cache dictionary) for O(1) access to cache items and a doubly linked list to maintain the items in order of use. This combination ensures constant-time operations for get, put, and removal of the least recently used item. Space efficiency is primarily governed by the cache's capacity, limiting the number of nodes and entries in the hash table, thus ensuring space usage grows linearly with the number of items up to the predefined capacity.

## Code Design
The design choices made in this LRU cache implementation include using a hash table for fast lookup and a doubly linked list for maintaining the order of elements based on usage. The Node class encapsulates the cache item and its position in the usage order, while the LRU_Cache class manages the overall cache operations. The choice of a doubly linked list allows for efficient removals and insertions at both ends, crucial for maintaining the LRU policy. The join helper method simplifies node connection and disconnection, contributing to the clarity and modularity of the code.
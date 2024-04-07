# 3.Huffman Coding

## Efficiency
The Huffman encoding and decoding processes exhibit distinct Big O time complexities across several operations. During encoding, the construction of the frequency table from the input data has a time complexity of O(n), with n representing the length of the input string, as the operation iterates over each character once. The creation of the min-heap from the frequency table is O(m log m), where m is the count of unique characters, since inserting into a heap is O(log m) for each unique character. Building the Huffman tree from the min-heap involves (m-1) iterations of removing two nodes and inserting one, each operation being O(log m), summing up to O(m log m) for the entire tree construction. Generating the binary codes by traversing the Huffman tree is O(m), as it entails a single visit to each unique character.

Decoding involves traversing the Huffman tree for each bit in the encoded data, translating to a time complexity of O(k), where k is the length of the encoded data. This step does not depend on the size of the original input data but on the size of the encoded string, which could be significantly smaller for repetitive data sets.

The space complexity primarily involves the storage for the frequency table, min-heap, and the Huffman tree, each requiring O(m) space, where m is the number of unique characters. Consequently, the total space complexity is O(m), influenced by the data structures holding unique characters and their frequencies.

In summary, the overall time complexity for Huffman encoding is O(n + m log m), combining the initial frequency table generation and subsequent heap and tree operations. The decoding process adds a time complexity of O(k), dependent on the encoded data length. The space complexity for both encoding and decoding is O(m), dictated by the structures storing unique characters.


## Code Design
The design employs a class heapNode to represent each node in the Huffman tree, capturing both the character and its frequency, along with pointers to left and right child nodes. The huffman_encoding function not only builds the Huffman tree but also generates the unique binary codes for each character, which are used to encode the input data. The huffman_decoding function then utilizes these codes to reconstruct the original data from the encoded binary string. The use of a heap to build the Huffman tree is a significant design choice that leverages the heap's properties to efficiently build the tree.
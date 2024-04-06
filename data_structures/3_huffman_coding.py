import sys
import heapq


###---- ENCODING ----###
class heapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        return self.freq == other.freq

def huffman_encoding(data):
    # Special case handling for empty input
    if not data:
        return "", None
    
    # Build Frequency Table
    frequency = {}
    
    for char in data:
        if frequency.get(char):
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Special case handling for single-character input
    if len(frequency) == 1:
        char = next(iter(frequency))  # Get the single character
        return "0" * frequency[char], heapNode(char, frequency[char])
    
    # Build minheap
    heap = []
    
    for key in frequency:
        node = heapNode(key, frequency[key])
        heapq.heappush(heap, node)
    
    # Build huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = heapNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
        
    # Create codes
    codes = {}
    root = heapq.heappop(heap)
    
    current_code = ""
    make_codes(root, current_code, codes)
    print(codes)
    
    # Encode Text
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
        
    return [encoded_data, root]

# Recursive helper function to create binary codes
def make_codes(node, current_code, codes):
    
    if(node==None):
        return

    if(node.char != None):
        codes[node.char] = current_code
    
    make_codes(node.left, current_code + "0", codes)
    make_codes(node.right, current_code + "1", codes)



###---- DECODING ----###
def huffman_decoding(data,tree):
    if not tree or not data:  # Check if the tree is None
        return ""
    
    # Special case for single-character encoding
    if tree.char is not None:
        return tree.char * len(data)
    
    decoded_text = ""
    current_node = tree
    
    for char in data:
        if char == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node and not current_node.left and not current_node.right:
            decoded_text += current_node.char
            current_node = tree
    
    return decoded_text




###---- TESTING ----###
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


## Test Case 1
    codes = {}

    weird_chars = "Weird Chars: !@#$%^&*()"

    print ("The size of the data is: {}\n".format(sys.getsizeof(weird_chars)))
    print ("The content of the data is: {}\n".format(weird_chars))

    encoded_data, tree = huffman_encoding(weird_chars)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Test Case 2
    codes = {}

    extra_long = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris facilisis metus quis cursus rhoncus. Maecenas egestas ornare leo. Nam sit amet aliquam tortor. Suspendisse vel eros imperdiet, finibus metus sed, ultricies dolor. Suspendisse non posuere lorem. In posuere mauris vel eros congue, id posuere odio eleifend. Fusce fringilla nunc quis faucibus bibendum. Nullam congue justo ac interdum lacinia. Cras sed iaculis dui, nec posuere quam. Etiam vitae vulputate tellus, nec condimentum ante. Etiam posuere pulvinar massa eget iaculis. Sed ac nisl a massa dictum rhoncus vel et enim. Nam metus odio, ultrices vitae felis in, commodo faucibus nunc. Nullam feugiat velit sed nisl lobortis, sit amet tristique odio sagittis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent laoreet quam mi, at imperdiet leo convallis eu."

    print ("The size of the data is: {}\n".format(sys.getsizeof(extra_long)))
    print ("The content of the data is: {}\n".format(extra_long))

    encoded_data, tree = huffman_encoding(extra_long)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
## Test Case 3: one_char
    codes = {}

    one_char = "f"

    print ("The size of the data is: {}\n".format(sys.getsizeof(one_char)))
    print ("The content of the data is: {}\n".format(one_char))

    encoded_data, tree = huffman_encoding(one_char)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

## Test Case 3: empty_string
    codes = {}

    empty_string = ""

    print ("The size of the data is: empty")
    print ("The content of the data is: {}\n".format(empty_string))

    encoded_data, tree = huffman_encoding(empty_string)

    print ("The size of the encoded data is: empty")
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: empty")
    print ("The content of the encoded data is: {}\n".format(decoded_data))
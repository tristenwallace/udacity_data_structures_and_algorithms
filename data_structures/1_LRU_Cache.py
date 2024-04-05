class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.item_count = 0
        self.cache = {} #key,node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.join(self.head, self.tail)
    
    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.remove(node)
            self.updateHead(node)
            return node.value
        return -1
        
    def put(self, key, value):
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.remove(node)
            self.updateHead(node)
            return
        
        if self.item_count == self.capacity:
            lastNode = self.tail.prev
            self.remove(lastNode)
            del self.cache[lastNode.key]
            self.item_count -= 1
        
        node = Node(key=key, value=value)
        self.updateHead(node)
        self.cache[key] = self.head.next  
        self.item_count += 1

    def join(self, node1: Node, node2: Node):
        node1.next = node2
        node2.prev = node1

    def remove(self, node: Node):
        self.join(node.prev, node.next)
    
    def updateHead(self, node: Node):
        self.join(node, self.head.next)
        self.join(self.head, node)
        


#-- TEST 1 --#
test_cache = LRU_Cache(5)

test_cache.put(1, 1)
test_cache.put(2, 2)
test_cache.put(3, 3)
test_cache.put(4, 4)

print(test_cache.get(1)) #print 1
print(test_cache.get(2)) #print 2
print(test_cache.get(9)) #print -1

test_cache.put(5, 5)
test_cache.put(6, 6)

print(test_cache.get(3)) #print -1,  because capacity is reached

#-- TEST 2 --#
test_cache = LRU_Cache(10000000000) # Test large cache
test_cache.put(1, 1)
print(test_cache.get(1))

#-- TEST 3 --#
test_cache = LRU_Cache(1)
test_cache.put(1, 1)
test_cache.put(1, 2)
test_cache.put(1, 3)
print(test_cache.get(1)) #print 3,  because that was most recent val
test_cache.put(3, 3)
print(test_cache.get(1)) #print -1,  because capacity is reached

#-- TEST 4 --#
test_cache = LRU_Cache(5)

test_cache.put(1, None)
print(test_cache.get(1)) # print None

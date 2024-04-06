class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def contains(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False


def union(llist_1, llist_2):
    result_set = set()
    union_ll = LinkedList()

    current_node = llist_1.head
    while current_node:
        result_set.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        result_set.add(current_node.value)
        current_node = current_node.next

    for value in result_set:
        union_ll.append(value)

    return union_ll


def intersection(llist_1, llist_2):
    set_1 = set()
    intersection_set = set()
    intersection_ll = LinkedList()

    current_node = llist_1.head
    while current_node:
        set_1.add(current_node.value)
        current_node = current_node.next

    current_node = llist_2.head
    while current_node:
        if current_node.value in set_1:
            intersection_set.add(current_node.value)
        current_node = current_node.next

    for value in intersection_set:
        intersection_ll.append(value)

    return intersection_ll



## Base case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
    
print("\nUnion:")
print (union(linked_list_1,linked_list_2))
print("\nIntersection:")
print (intersection(linked_list_1,linked_list_2))

## Base case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nUnion:")
print (union(linked_list_3,linked_list_4))
print("\nIntersection:")
print (intersection(linked_list_3,linked_list_4))


## Test Case 1: No Common Elements
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [4, 5, 6]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)

print("\nTest Case 1: No Common Elements")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))

## Test Case 2: One List is Empty
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []

element_2 = [1, 2, 3]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)

print("\nTest Case 2: One List is Empty")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))

## Test Case 3: All Elements in Common
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3]
element_2 = [1, 2, 3]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)

print("\nTEST 3: All Elements in Common")
print("Union:", union(linked_list_1, linked_list_2))
print("Intersection:", intersection(linked_list_1, linked_list_2))
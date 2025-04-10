class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [None] * self.capacity

    def resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def prepend(self, value):
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, 0, -1):  # shift right
            self.arr[i] = self.arr[i - 1]
        self.arr[0] = value
        self.size += 1

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1


class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL_Deque:
    def __init__(self):
        self.header = DLL_Node("header")
        self.trailer = DLL_Node("trailer")
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def push_back(self, value):
        new_node = DLL_Node(value)
        last = self.trailer.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.trailer
        self.trailer.prev = new_node

    def ContainsValue(self, value):
        current = self.header.next
        while current != self.trailer:
            if current.data == value:
                return True
            current = current.next
        return False

class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def Length(head):
    if head is None:
        return 0
    return 1 + Length(head.next)

class HashMap:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.bucket_arr = [Bucket() for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def remove(self, key):
        index = self._hash(key)
        bucket = self.bucket_arr[index]
        if bucket.contains(key):
            bucket.remove(key)
            self.size -= 1

    def contains(self, key):
        index = self._hash(key)
        return self.bucket_arr[index].contains(key)

    def find(self, key):
        index = self._hash(key)
        return self.bucket_arr[index].find(key)
class BSTNode:
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        def _insert(node, key, data):
            if node is None:
                return BSTNode(key, data)
            if key == node.key:
                return node  # Key already exists, do nothing
            elif key < node.key:
                node.left = _insert(node.left, key, data)
            else:
                node.right = _insert(node.right, key, data)
            return node

        if self.find(key) is None:
            self.root = _insert(self.root, key, data)
            self.size += 1

    def find(self, key):
        def _find(node, key):
            if node is None:
                return None
            if key == node.key:
                return node.data
            elif key < node.key:
                return _find(node.left, key)
            else:
                return _find(node.right, key)
        return _find(self.root, key)

    def update(self, key, data):
        def _update(node, key, data):
            if node is None:
                return
            if key == node.key:
                node.data = data
            elif key < node.key:
                _update(node.left, key, data)
            else:
                _update(node.right, key, data)
        _update(self.root, key, data)

    def count_odd_elements(self):
        return self.count_odd_elements_recur(self.root)

    def count_odd_elements_recur(self, node):
        if node is None:
            return 0
        count = 1 if node.key % 2 == 1 else 0
        return count + self.count_odd_elements_recur(node.left) + self.count_odd_elements_recur(node.right)
class DLL_Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.header = DLL_Node("header")
        self.trailer = DLL_Node("trailer")
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.curr = self.trailer  # current starts at the end
        self.size = 0

    def insert(self, value):
        new_node = DLL_Node(value)
        prev_node = self.curr.prev
        new_node.prev = prev_node
        new_node.next = self.curr
        prev_node.next = new_node
        self.curr.prev = new_node
        self.curr = new_node
        self.size += 1

    def clear(self):
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.curr = self.trailer
        self.size = 0

    def move_to_pos(self, position):
        if position < 0 or position >= self.size:
            return  # Do nothing
        self.curr = self.header.next
        for _ in range(position):
            self.curr = self.curr.next
class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        new_node = SLL_Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:  # list became empty
            self.tail = None
        return value

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " ".join(result)

def mystery_function(n):
    if n <= 0:
        return 0
    return n + mystery_function(n - 1)

print(mystery_function(5))  # Output: 15

def power(base, exp):
    if exp == 1:
        return base
    return base * power(base, exp - 1)
  
class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [None] * self.capacity

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.size - 1] = None
        self.size -= 1

    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    def resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def __str__(self):
        return ", ".join(str(self.arr[i]) for i in range(self.size))



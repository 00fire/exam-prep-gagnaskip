Absolutely! Here's a **clear cheat sheet with basic examples** of:

- **Stacks**
- **Queues**
- **Heaps**

---

## 🥞 **Stacks (LIFO - Last In, First Out)**

### ✅ Basic Stack Operations:
- `push(item)` → Add to top  
- `pop()` → Remove from top  
- `peek()` → View top item  
- `is_empty()` → Check if stack is empty

### ✅ Implementation with Python List:
```python
stack = []

# Push
stack.append(10)
stack.append(20)

# Pop
print(stack.pop())  # 20

# Peek
print(stack[-1])    # 10

# Is Empty
print(len(stack) == 0)  # False
```

### ✅ Custom Stack Class:
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if self.items else None
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
```

---

## 🚶‍♂️🚶 **Queues (FIFO - First In, First Out)**

### ✅ Basic Queue Operations:
- `enqueue(item)` → Add to back  
- `dequeue()` → Remove from front  
- `peek()` → View front item  
- `is_empty()` → Check if queue is empty

### ✅ Using `collections.deque`:
```python
from collections import deque

queue = deque()

# Enqueue
queue.append(1)
queue.append(2)

# Dequeue
print(queue.popleft())  # 1

# Peek
print(queue[0])  # 2

# Is Empty
print(len(queue) == 0)  # False
```

### ✅ Custom Queue Class:
```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def peek(self):
        return self.items[0] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
```

---

## 🔺 **Heaps (Priority Queues)**

- **Min Heap**: smallest item at root
- **Max Heap**: Python doesn't support this directly, but can be simulated

### ✅ Using `heapq` for Min-Heap:
```python
import heapq

heap = []

# Add elements
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 9)

# Pop smallest
print(heapq.heappop(heap))  # 2

# Peek smallest
print(heap[0])  # 5
```

### ✅ Max Heap using `-value` trick:
```python
import heapq

max_heap = []

# Push negative values to simulate max-heap
heapq.heappush(max_heap, -1 * 10)
heapq.heappush(max_heap, -1 * 30)

# Get max
print(-1 * heapq.heappop(max_heap))  # 30
```

---

Would you like **visuals** or **challenge questions** on these to practice too
?
Absolutely! Here's a handy **Time Complexity Cheat Sheet** for:

- 🥞 **Stacks**
- 🚶 **Queues**
- 🔺 **Heaps**

---

## 🥞 **Stack Time Complexity (using Python list)**
| Operation     | Time Complexity |
|---------------|------------------|
| `push()`      | O(1)             |
| `pop()`       | O(1)             |
| `peek()`      | O(1)             |
| `is_empty()`  | O(1)             |

> ✅ Efficient since you're working at the **end** of the list.

---

## 🚶 **Queue Time Complexity**
### Using `collections.deque` (recommended):
| Operation      | Time Complexity |
|----------------|------------------|
| `enqueue()`    | O(1)             |
| `dequeue()`    | O(1)             |
| `peek()`       | O(1)             |
| `is_empty()`   | O(1)             |

### Using list (⚠️ less efficient):
| Operation    | Time Complexity |
|--------------|------------------|
| `enqueue()`  | O(1)             |
| `dequeue()`  | O(n)             | ← because popping from front shifts all items

---

## 🔺 **Heap Time Complexity** (`heapq`)
| Operation            | Time Complexity |
|----------------------|------------------|
| `heappush()`         | O(log n)         |
| `heappop()`          | O(log n)         |
| `peek` (heap[0])     | O(1)             |
| Building a heap      | O(n)             |

> ✅ `heapq` maintains a **binary heap**, not a binary search tree.

---

### Summary Table:

| Data Structure | Insert | Delete | Search | Peek |
|----------------|--------|--------|--------|------|
| Stack          | O(1)   | O(1)   | O(n)   | O(1) |
| Queue (deque)  | O(1)   | O(1)   | O(n)   | O(1) |
| Heap           | O(log n)| O(log n) | O(n) (unsorted) | O(1) |

---

Let me know if you want **linked list**, **array**, or **BST** time complexity too — or a printable version!

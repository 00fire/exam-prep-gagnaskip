Sure! Here’s a **quick cheat sheet** of the most **basic recursion operations** you need to know, especially for linked lists and trees (which are common in data structures exams like Gagnaskipan).

---

## 🔁 Basic Recursion Operations Cheat Sheet

### 1. **Recursively Print Numbers (1 to n)**
```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
```

---

### 2. **Sum of First `n` Natural Numbers**
```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
```

---

### 3. **Length of a Singly Linked List (Recursive)**  
```python
def Length(head):
    if head is None:
        return 0
    return 1 + Length(head.next)
```

---

### 4. **Search in Linked List**
```python
def contains_value(head, value):
    if head is None:
        return False
    if head.data == value:
        return True
    return contains_value(head.next, value)
```

---

### 5. **Nth from End (Recursive Helper)**  
```python
def nth_from_end(head, n):
    def helper(node, n):
        if node is None:
            return (0, None)
        count, value = helper(node.next, n)
        if count == n:
            return (count + 1, node.data)
        return (count + 1, value)
    
    return helper(head, n)[1]
```

---

### 6. **Recursively Reverse a Linked List**
```python
def reverse_list(head):
    if head is None or head.next is None:
        return head
    rest = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return rest
```

---

### 7. **Binary Tree Height**
```python
def height(root):
    if root is None:
        return -1  # or 0 depending on definition
    return 1 + max(height(root.left), height(root.right))
```

---

### 8. **In-order Traversal (Tree)**
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
```

---

### 9. **Factorial**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

### 10. **Fibonacci**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

Want these saved in a printable PDF, or want examples for doubly linked lists or trees too?

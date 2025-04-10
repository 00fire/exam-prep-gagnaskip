class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)

def nth_from_end(head, n):
    pass

class SentenceTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = []

class SentenceTree:
    def __init__(self):
        self.root = SentenceTreeNode("")
    
    def store_sentence(self, sentence):
        #this line helps you match the sentence to the tree structure
        sentence_list = sentence.split()

    def contains_sentence(self, sentence):
        #the lines below help you match the sentence to the tree structure
        sentence_list = sentence.split()
        sentence_list = [""] + sentence_list #this "" is added to match the root to start with
        #your code here

if __name__ == "__main__":
    print("testing nth from end")
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 0))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 1))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 2))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 3))
    sllhead = SLL_Node(6, SLL_Node(1, SLL_Node(5, SLL_Node(4, SLL_Node(9, SLL_Node(8))))))
    print(nth_from_end(sllhead, 4))
    print("testing sentence tree")
    sentences = SentenceTree()
    #you might want to comment out some of these temporarily when testing
    sentences.store_sentence("my name is jeff")
    print("1", sentences.contains_sentence("my name"))
    print("2", sentences.contains_sentence("my dog"))
    sentences.store_sentence("my dog is happy")
    print("3", sentences.contains_sentence("my dog"))
    print("4", sentences.contains_sentence("my jeff"))
    sentences.store_sentence("my name doesn't concern you")
    sentences.store_sentence("my name is jeff also")
    print("5", sentences.contains_sentence("concern you"))
    print("6", sentences.contains_sentence("my name is"))
    print("7", sentences.contains_sentence("my name is jeff also"))
    print("8", sentences.contains_sentence("jeff"))
    sentences.store_sentence("jeff is happy")
    sentences.store_sentence("jeff is a dog")
    print("9", sentences.contains_sentence("jeff"))
    print("10", sentences.contains_sentence("jeff is dog"))
    print("11", sentences.contains_sentence("jeff is a dog"))
    print("12", sentences.contains_sentence("jeff is a happy dog"))
    print("13", sentences.contains_sentence("jeff is happy"))
    print("14", sentences.contains_sentence("jeff is a dog also"))



class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def nth_from_end(head, n):
    def helper(node):
        if node is None:
            return 0, None
        index, result = helper(node.next)
        if index == n:
            return index + 1, node
        return index + 1, result

    _, target_node = helper(head)
    return target_node.data if target_node else None
class TreeNode:
    def __init__(self, word=""):
        self.word = word
        self.children = {}

class SentenceTree:
    def __init__(self):
        self.root = TreeNode()
    def store_sentence(self, sentence):
        current = self.root
        words = sentence.split()

        for word in words:
            if word not in current.children:
                current.children[word] = TreeNode(word)
            current = current.children[word]
    def contains_sentence(self, sentence):
        current = self.root
        words = sentence.split()

        for word in words:
            if word not in current.children:
                return False
            current = current.children[word]
        return True


class TreeNode:
    def __init__(self, word=""):
        self.word = word
        self.children = {}

class SentenceTree:
    def __init__(self):
        self.root = TreeNode()

    def store_sentence(self, sentence):
        current = self.root
        words = sentence.split()

        for word in words:
            if word not in current.children:
                current.children[word] = TreeNode(word)
            current = current.children[word]

    def contains_sentence(self, sentence):
        current = self.root
        words = sentence.split()

        for word in words:
            if word not in current.children:
                return False
            current = current.children[word]
        return True

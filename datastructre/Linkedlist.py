class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

    def insertnode(self, key):
        t = self.next
        self.next = Node(key)
        self.next.next = t

    def delnode(self):
        self.next = self.next.next

    def getnext(self):
        return self.next


def traversal(node):
    if node is not None:
        print(node.key)
        traversal(node.next)


if __name__=='__main__':
    root = Node(0)
    for i in range(10):
        root.insertnode(10-i)
    root.delnode()
    traversal(root)

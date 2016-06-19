class Binarytree:
    def __init__(self, obj):
        self.key = obj
        self.leftChild = None
        self.rightChild = None

    def insertlift(self, node):
        if self.leftChild is None:
            self.leftChild = Binarytree(node)
        else:
            t = Binarytree(node)
            t.leftChild = self.leftChild
            self.leftChild = t.leftChild

    def insertright(self, node):
        if self.rightChild is None:
            self.rightChild = Binarytree(node)
        else:
            t = Binarytree(node)
            t.rightChild = self.rightChild
            self.rightChild = t.rightChild

    def removeleft(self):
        t = self.leftChild.leftChild
        del self.leftChild
        self.leftChild = t

    def removeright(self):
        t = self.rightChild.rightChild
        del self.rightChild
        self.rightChild = t

    def getkey(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild is not None:
            self.leftChild.preorder()
        if self.rightChild is not None:
            self.rightChild.preorder()


def inorder(root):
    if root is not None:
        if root.leftChild is not None:
            inorder(root.leftChild)
        print(root.key)
        if root.rightChild is not None:
            inorder(root.rightChild)


if __name__ == '__main__':
    root = Binarytree(0)
    root.insertlift(1)
    root.insertright(2)
    l = root.leftChild
    r = root.rightChild
    l.insertlift(3)
    l.removeleft()
    l.insertright(4)
    r.insertlift(5)
    r.insertright(6)
    print('preorder:')
    root.preorder()
    print('inorder:')
    inorder(root)

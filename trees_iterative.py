class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,key):
        if self.root == None:
            self.root = Node(key)
        # iterative approach
        curr = self.root
        while True:
            if key < curr.val:
                if curr.left is None:
                    curr.left = Node(key)
                    return
                curr = curr.left
            elif key > curr.val:
                if curr.right is None:
                    curr.right = Node(key)
                    return
                curr = curr.right
            else:
                return

    def inorder(self):
        res = []
        curr = self.root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

    def delete(self,key):
        parent = None
        curr  = self.root
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None :
            return self.root
        if curr.left is None:
            temp = curr.right
            if parent is None :
                self.root = temp
            elif parent.left == curr:
                parent.left = temp
            else:
                parent.right = temp
            curr = None
        elif curr.right is None:
            temp = curr.right
            if parent is None:
                self.root = temp
            elif parent.left == curr:
                parent.left = temp
            else:
                parent.right = temp
            curr = None
        else:
            sp = curr
            s = curr.right
            while s.left is not None:
                sp = s
                s = s.left
            curr.val = s.val
            if sp.left == s:
                sp.left = s.right
            if sp.right == s:
                sp.right = s.right
        return self.root

if __name__ == '__main__':
    tree = BinaryTree()
    nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for n in nodes_to_insert:
        tree.insert(n)
    print("Initial In-order traversal:", tree.inorder())
    key = 20
    #is below statement is needed?
    tree.root = tree.delete(key)
    print("Final In-order traversal:", tree.inorder())


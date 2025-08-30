class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class binary_trees:
    def __init__(self):
        self.root = None
    def insert(self,key):
        self.root = self._insert_aux(self.root,key)
    def _insert_aux(self,node,key):
        if node is None:
            return Node(key)
        if key < node.val:
            node.left = self._insert_aux(node.left,key)
        if key > node.val:
            node.right = self._insert_aux(node.right,key)
        return node

    def search(self,key):
        return self._search_aux(self.root,key)
    def _search_aux(self,root,key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_aux(root.left,key)
        if key > root.val:
            return self._search_aux(root.right,key)

    def inorder_traversal(self):
        res = []
        self._inorder_rec(self.root,res)
        return res
    def _inorder_rec(self,root,res):
        if root :
            self._inorder_rec(root.left,res)
            res.append(root.val)
            self._inorder_rec(root.right,res)

    def delete_(self,key):
        self.root = self._delete_aux(self.root, key)
    def _delete_aux(self,root,key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete_aux(root.left,key)
        elif key > root.val:
            root.right = self._delete_aux(root.right,key)
        # this happens when we find the key in tree above code is for searching the key
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self._get_min(root.right)
            root.val = temp.val
            root.right = self._delete_aux(root.right,temp.val)
        return root
    def _get_min(self,node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

if __name__ == '__main__':
    bst = binary_trees()
    Nodes = [50, 30, 70, 20, 40, 60, 80]
    for n in Nodes:
        bst.insert(n)

    print("we are traversing...",bst.inorder_traversal())
    key = 30
    found = bst.search(key)
    if found:
        print(f"found {key}")
    else:
        print(f"not found {key}")





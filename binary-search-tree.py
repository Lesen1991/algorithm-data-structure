class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.balance = 0


root = TreeNode(7)
n1 = TreeNode(2)
n1.parent = root
root.left = n1
n2 = TreeNode(10)
n2.parent = root
root.right = n2
n3 = TreeNode(1)
n3.parent = n1
n1.left = n3
n4 = TreeNode(5)
n4.parent = n1
n1.right = n4
n5 = TreeNode(9)
n5.parent = n2
n2.left = n5


def search_binary_tree(r, val):
    if r is None:
        return None
    if r.val == val:
        return r
    if r.val > val:
        return search_binary_tree(r.left, val)
    else:
        return search_binary_tree(r.right, val)


def traverse_binary_tree(r):
    if r is None:
        return
    traverse_binary_tree(r.left)
    print(r.val)
    traverse_binary_tree(r.right)


print(traverse_binary_tree(root))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)

def search(curr: TreeNode, number: int):
    if not curr:
        return False
    if curr.val > number:
        return search(curr.left, number)
    elif curr.val < number:
        return search(curr.right, number)
    else:
        return True

res = search(root, 5)
print(res)




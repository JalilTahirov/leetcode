class TreeNode:
    def __init__(val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

# leetcode

* My leetcode DSA preparation notes and solved problems
* Namming example  python/0001-two-sum.py


[0001 two-sum](https://github.com/JalilTahirov/leetcode/blob/main/python/0001-two-sum.py)

```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store seen numbers and their corresponding indices
        map = {}

        # Loop through each element in the list
        for i in range(len(nums)):
            x = nums[i]
            y = target - x

            # Check if the complement has already been seen in the list
            if x in map:
                # If yes, we've found a pair that adds up to the target
                return [i, map[x]]
            else:
                # If not, add the current number and its index to the dictionary
                map[y] = i


```

[0015 3 sum](https://github.com/JalilTahirov/leetcode/blob/main/python/0015-3sum.py)

[0143 reorder List](https://github.com/JalilTahirov/leetcode/blob/main/python/0143-reorder-list.py)

[0455-assign cookies](https://github.com/JalilTahirov/leetcode/blob/main/python/0455-assign-cookies.py)

[1984-minimum-difference-between-highest-and-lowest-of-k-scores](https://github.com/JalilTahirov/leetcode/blob/main/python/1984-minimum-difference-between-highest-and-lowest-of-k-scores.py)


[0680-valid polindrome](https://github.com/JalilTahirov/leetcode/blob/main/python/0680-valid-palindrome-ii.py)


## 98 Validate Binary Search Tree

> Given the root of a binary tree, determine if it is a valid binary search tree (BST).
> A valid BST is defined as follows:
> The left subtree of a node contains only nodes with keys less than the node's key.
> The right subtree of a node contains only nodes with keys greater than the node's key.
> Both the left and right subtrees must also be binary search trees.
> Example 1:
> Input: root = [2,1,3]
>Output: true
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isValidHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if (val > low and val < high) and self._isValidHelper(n.left, low, n.val) and self._isValidHelper(n.right, n.val, high):
            return True
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidHelper(root, float('-inf'), float('inf'))
```






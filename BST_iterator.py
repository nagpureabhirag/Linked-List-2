# Did this code successfully run on Leetcode : YES

# TC: O(1)
# SC: O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.dfs(root)


    def next(self) -> int:
        res = self.stack.pop()
        self.dfs(res.right)
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
    
    def dfs(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#tc: O(n)
#sc: O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # limits approach
    def __init__(self):
        self.flag = True      
    
    def isValidBST(self, root) -> bool:
        def helper(root,minlimit,maxlimit):
            #base
            if root is None: return
            if root.val <= minlimit:
                self.flag = False
            if root.val >= maxlimit:
                self.flag =  False
            #logic
            helper(root.left,minlimit,root.val)
            if self.flag: # optimisation
                helper(root.right,root.val,maxlimit)
        
        helper(root,float('-inf'),float('inf'))
        return self.flag
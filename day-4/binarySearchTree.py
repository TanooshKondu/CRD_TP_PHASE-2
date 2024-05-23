#Binary search Tree
#leetcode 701
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if root == None:
#             return TreeNode(val)
#         elif root.val > val:
#             root.left = self.insertIntoBST(root.left, val)
#         else:
#             root.right = self.insertIntoBST(root.right, val)
#         return root

#<<<<<<<<-----Delete BST------>>>>>>>>>>
#leetcode 450, 700
#https://pastebin.com/tBYc8fJb

def findInorderPredessor(root):
    while root.left != None:
        root = root.left 
    return root.data

def deleteInBST(root, val):
    if root == None:
        return None 
    elif root.data > val:
        root.left = deleteInBST(root.left, val)
    elif root.data < val:
        root.right = deleteInBST(root.right, val)
    else:
        if root.left == None and root.right == None:
            return None 
        elif root.left == None:
            return root.right 
        elif root.right == None:
            return root.left 
        else:
            predessor = findInorderPredessor(root)
            root.data = predessor 
            root.right = deleteInBST(root.right, predessor)
        return root
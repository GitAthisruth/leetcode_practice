# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

#  Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:


# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# nums = [-10,-3,0,5,9]

# m = min(nums)

# m = filter(lambda x:x==0,nums)

# print(list(m)) #map will give you a boolean while filter will give you the real value.map apply on Series,apply works on both series and dataframe and applymap only works on dataframe.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# class Solution(object):
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: Optional[TreeNode]
#         """
#         if not nums:
#             return None
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root

# sol = Solution()

# root = sol.sortedArrayToBST(nums)

# print(root)

nums = [-10,-3,0,5,9]

# my way of approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left =  array_to(nums[:mid])
    root.right = array_to(nums[mid+1:])
    # print(root,root.left,root.right)
    return root

print(array_to(nums))   




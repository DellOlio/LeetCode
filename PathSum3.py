''' 
dan nam je root binary tree-a i integer targetSum
vracamo broj putanja gdjde je suma vrijednost jednaka targetSum
ne mora pocet na root ali mora ic prema dolje
'''


from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self,root,targetSum):
        
        dictionaryOfOptions = defaultdict(int)
        dictionaryOfOptions[0]=1
        return self.helper(root,0,dictionaryOfOptions,targetSum)
    def helper(self,root,currentSum,dictionaryOfOptions,targetSum):
        if root == None:
            return
            
        currentSum += root.val

        count = dictionaryOfOptions[targetSum-currentSum]

        dictionaryOfOptions[currentSum]+=1



        count+=self.helper(root.right,currentSum,dictionaryOfOptions,targetSum)
        count+=self.helper(root.left,currentSum,dictionaryOfOptions,targetSum)

        dictionaryOfOptions[currentSum]-=1
        if dictionaryOfOptions[currentSum]==0:
            del dictionaryOfOptions[currentSum]    
        return count

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    
#         self.total = 0
#         def helper(root,curTotal):
#             if root == None:
#                 return
#             if curTotal+root.val == targetSum:
#                 self.total+=1
#             helper(root.right,curTotal+root.val)
#             helper(root.left,curTotal+root.val)


#         def dfs(root):
#             if root == None:
#                 return
#             helper(root,0)

#             dfs(root.left)
#             dfs(root.right)
#         dfs(root)
#         return self.total


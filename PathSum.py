'''
Dan nam je root i int targetSum
vracamo true ako ima root-to-leaf putanja koja je kada je sumirana je jednaka targetSum
leaf je node bez dijece

'''


class Solution:
    output=False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def PathSum(root,targetSum,curSum):
            if root==None or self.output==True:
                return
            
            curSum+=root.val
            PathSum(root.left,targetSum,curSum)
            PathSum(root.right,targetSum,curSum)


            if root.left==None and root.right== None and curSum==targetSum:
                self.output = True
        PathSum(root,targetSum,0)
        return self.output


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def PathSum(root,targetSum,curSum):
            if root==None:
                return False
            curSum+=root.val

            if curSum==targetSum and root.left==None and root.right==None:
                return True
            if root.left!=None:
                if PathSum(root.left,targetSum,curSum)==True:
                    return True
            if root.right !=None:
                if PathSum(root.right,targetSum,curSum)==True:
                    return True
            return False
        return PathSum(root,targetSum,0)

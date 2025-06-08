'''

dana su nam dva drva i trebamo vidjet jesu li slicni
drva su slicna ako su njihove najnize vrijednosti iste
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

null = None
root1 = [3,5,1,6,2,9,8,null,null,7,4]
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]




def leafSimilar(root1,root2):
    def leafValues(root,leafValues):
        if root == None:
            return None
        if(root.left==None and root.right==None ):
            leafValues.append(root)
        leafValues(root.left,leafValues)
        leafValues(root.right,leafValues)
    root1Values=[]
    root2Values=[]

    leafValues(root1,root1Values)
    leafValues(root2,root2Values)

    return root1Values==root2Values
    


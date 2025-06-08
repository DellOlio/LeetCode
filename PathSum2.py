'''
Dan nam je root binary tree-a i int targetSum.
Vracamo sve root-to-leaf putanje gdje je suma  vrijednosti jednaka target-sumi.
Svaka lista treba bit vracena kao lista vrijednosti a ne lista TreeNode-ova.
Root-to-leaf je od roota do dna.

'''

class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        outputList=[]
        def helper(root,listOfValues,currentSum):
            if root == None:
                return
            
            

            listOfValues.append(root.val)
            currentSum+=root.val
            if(root.left ==None and root.right ==None and currentSum==targetSum):
                outputList.append(list(listOfValues))
            helper(root.left,listOfValues,currentSum)
            helper(root.right,listOfValues,currentSum)

            listOfValues.pop()
            


        helper(root,[],0)
        return outputList
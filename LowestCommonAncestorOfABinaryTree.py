'''
najmanje zajednicki predak je definiran izmedu dva node-a p i q kao najmanji node u T koji ima i p i q kao predake
dopustamo node-ovima da budu sami sebi predaci

'''

#
def lowestCommonAncestor(root,p,q):
    
    def helper(root):
        if not root:
            return None
        if root ==q or root == p:
            return True
        

        left = helper(root.left)
        right= helper(root.right)



        if left and right:
            return root
        elif left and not right:
            return left
        else:
            return right
    helper(root)

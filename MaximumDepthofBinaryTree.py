'''
dan nam je root binary tree-a i trebamo vratit najveci depth
to je broj node-ova po najduzoj putanjii od root-a do najdaljeg node-a


'''

#koristimo rekurziju
root = [3,9,20,None,None,15,7] #ovo je samo za sliku zapravo to tako ne izgleda
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root):
    if root == None:
        return 0
    maxLeft = maxDepth(root.left)
    maxRight = maxDepth(root.right)
    return 1+max(maxLeft,maxRight)



def maxDepth(root):
    if root == None:
        return 0
    
    level = 0
    deque = [root]
    while deque:
        for i in range(len(deque)):
            node = deque.pop(0)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
            
        level+=1



    return level

def maxDepth(root):
    stack = [[root,1]]
    res = 0

    while stack:
        node,depth = stack.pop()
        if node:
            res = max(res,depth)
            stack.append([node.right,depth+1])
            stack.append([node.left,depth+1])
    return res

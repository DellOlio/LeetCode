'''
Dan nam je root i trebamo se zamisliti na desnoj strani od drveta
vracamo vrijednosti najblize nama
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if root == None:
        return []
    res=[]
    deque = []
    deque.append(root)
    while deque:
        rightNode = None
        for i in range(len(deque)):
            node = deque.pop(0)
            if node:
                if node.left != None:
                    deque.append(node.left)
                if node.right != None:
                    deque.append(node.right)
                rightNode=node.val
        if rightNode!=None:
            res.append(rightNode)
    
    return res



            
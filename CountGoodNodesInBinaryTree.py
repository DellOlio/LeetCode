'''
dan nam je binary tree root
node x je dobar ako putanja od root-a do x nema nikoje vrijednosti vece od x
vracamo broj dobrih node-ova

'''
null = None
root = [3,1,4,3,null,1,5]


def goodNodes(root):
    leafs = []
    def goodNodesCount(root,leafs,maxVal=0):
        if root == None:
            return
        if root.val >=maxVal:
            leafs.append(root.val)
            maxVal = root.val
        goodNodesCount(root.left,leafs,maxVal)
        goodNodesCount(root.right,leafs,maxVal)
        
    goodNodesCount(root,leafs)
    return len(leafs)


def goodNodes(root):
    def goodNodesCount(root,maxVal):
        if root == None:
            return 0
        
        k= 0
        maxVal = max(maxVal,root.val)
        if root.val >= maxVal:
            k+=1
        k+=goodNodesCount(root.left,maxVal)
        k+=goodNodesCount(root.right,maxVal)
        return k
    return goodNodesCount(root,root.val)
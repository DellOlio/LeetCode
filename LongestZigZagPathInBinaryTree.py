'''
biramo bilo koji node u binary tree-u ako je trenutna putanj desno idemo desno inace lijevo
mjenjamo putanju sa desno na lijevo ili obrnuto
ponavljamo korake dok se ne mozemo vise micat
zigzag duzina je definirana kao broj posjecenih node-ova -1(ako je samo jedan node to je 0)
vracamo najduzu zigzag putanju
'''



def longestZigZag(root):
    maxZigZag = 0
    def helper(root,direction="root",lenght=0):
        nonlocal maxZigZag
        if root == None:
            return
        
        maxZigZag=max(maxZigZag,lenght)

        if direction=="right":
            helper(root.left,"left",lenght+1)
            helper(root.right,"right",0)
        elif(direction == "left"):
            helper(root.left,"left",0)
            helper(root.right,"right",lenght+1)
        else:
            helper(root.left,"left",lenght+1)
            helper(root.right,"right",lenght+1)


    helper(root)
    return maxZigZag




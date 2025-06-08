'''
u linked listi velicine n gdje je n paran broj i i-ti node(0-indexed) je blizanac sa node-om n-1-i ako je 0<=i<=(n/2)-1
twin sum je sum ta dva broja
dan nam je head linked liste i trebamo vratit najveci twin
'''

# head = [5,4,2,1]
# def pairSum(head):
#     temp = []
#     maxVal=0
#     start = 0
#     end = 0
#     while head:
#         temp.append(head)
#         head = head.next
#     for i in range (len(temp)/2):
#         start = temp[i]
#         end = temp[len(temp)-1-i]
#         maxVal = max(maxVal,start+end)
#     return maxVal


#trebamo nac polu liste sa fast i slow pointerom
#onda trebamo toj drugoj poli zamjenit redosljed
#i onda ih usporedit
head = [5,4,2,1,2,4,1,2]
      # s s s s s
      # f   f   f   f   f
def pairSum(head):
    fast = head
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next.next
    
    slowLinkedList = None

    while slow:
        nextNode = slow.next
        slow.next = slowLinkedList
        slowLinkedList = slow
        slow = nextNode
    MaxValue = 0
    while slowLinkedList:
        MaxValue = max(MaxValue,slowLinkedList.val+head.val)
        slowLinkedList = slowLinkedList.next
        head = head.next
    return MaxValue






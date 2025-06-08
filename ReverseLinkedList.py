'''
Trebamo obrnut redosljed linked liste 


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




head = [1,2,3,4,5]

def reverseList(head):
    resultList = None
    current = head
    while current:
        nextNode = current.next
        current.next = resultList
        resultList = current
        current = nextNode
    return resultList
        
    
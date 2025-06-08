'''
1.dan nam je head linked liste.
2.trebamo izbrisat srednji node i vratit head node
3.srednji node je n/2 sa n len(linked_list)(zaokruzujemo na manje)


'''




 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5) 

def deleteMiddle(head):
    if head == None:
        return None

    dummy = slow = fast = ListNode(0)
    dummy.next = head
    while(fast.next!=None and fast.next.next!=None):
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next

    return dummy.next

        


    
    



new_head = deleteMiddle(head)
printList(new_head)
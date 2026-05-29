from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        temp = 0

        while current and current.next:
            

            if current.val == current.next.val:
                current.next = current.next.next
                temp = 1
            elif(temp == 1):
                if previous is not None:
                    previous.next = current.next
                else: previous = None  
                if head is current:
                    head = current.next  
                current = current.next  
                temp = 0
            else:
                previous = current
                current = current.next


        if temp == 1:
            if previous is not None:
                    previous.next = current.next
            else: previous = None  
            if head is current:
                head = current.next  
            current = current.next  
            temp = 0

        return head   
# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find half of linked list
        fast, slow = head.next, head
        # check if fast is reached end if odd or it 
        # will reach end on next if even
        while fast and fast.next:
            slow = slow.next # grow slow with one step
            fast = fast.next.next # grow fast with 2 steps
        #print(slow.val)

        prev, curr, next= None, slow.next, None
        while curr:
            
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        first = head
        second=prev
        next_1, next_2 = None, None

        while first and second.next:
            next_1 = first.next
            next_2 = second.next
            first.next = second
            second.next = next_1
            second = next_2
            first =next_1


        head = first






        



myList = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6, ListNode(7)))))))

Solution.reorderList(Solution, myList)
while myList:
    print(myList.val)
    myList = myList.next
        

        
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2:ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                dig1 = l1.val 
            else:
                dig1 = 0
            if l2 is not None:
                dig2 = l2.val 
            else:
                dig2 = 0

            sum = dig1 + dig2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummyHead.next
        dummyHead.next = None
        return result





        
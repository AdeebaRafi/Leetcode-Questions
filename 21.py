# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # Temporary dummy node
        tail = dummy  # Tail points to the end of the merged list

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes (if any)
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # The merged list starts after the dummy

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        step1 = head
        step2 = head

        while step2 is not None and step2.next is not None:
            step1 = step1.next
            step2 = step2.next.next
        return step1
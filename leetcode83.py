class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==None:
            return head
        team = head
        while team.next != None:
            if team.val == team.next.val:
                team.next = team.next.next
            else:
                team = team.next
        return head
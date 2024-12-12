class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both linked lists
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0  # Get value from l1 or 0 if None
            y = l2.val if l2 is not None else 0  # Get value from l2 or 0 if None
            total = carry + x + y
            carry = total // 10  # Update carry for next addition
            current.next = ListNode(total % 10)  # Create new node with sum % 10
            current = current.next  # Move to the next node

            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        # If there's a leftover carry, add a new node
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

# Helper function to convert a list to a linked list
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
sol = Solution()

# Test Case 1
l1 = to_linked_list([2, 4, 3])  # Represents 342
l2 = to_linked_list([5, 6, 4])  # Represents 465
result = sol.addTwoNumbers(l1, l2)
print("Input: l1 = [2, 4, 3], l2 = [5, 6, 4]")
print("Output:", to_list(result))



#leetcode
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0
#
#         while l1 is not None or l2 is not None:
#             x = l1.val if l1 is not None else 0
#             y = l2.val if l2 is not None else 0
#             sum = carry + x + y
#             carry = sum // 10
#             current.next = ListNode(sum % 10)
#             current = current.next
#
#             if l1 is not None: l1 = l1.next
#             if l2 is not None: l2 = l2.next
#
#         if carry > 0:
#             current.next = ListNode(carry)
#
#         return dummy.next


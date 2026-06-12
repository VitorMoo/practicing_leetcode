# class ListNode:
#     def __init__(self, val=0, next=None):
#         # Each node contains a value and a pointer to the next node
#         self.val = val
#         self.next = next


#first solution:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_nodes = 0
        current = head
        while current is not None:
            total_nodes += 1
            current = current.next
            
        middle_index = total_nodes // 2
        
        current = head
        for _ in range(middle_index):
            current = current.next
            
        return current

#best solution:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two-Pointer Technique
        fast = head
        slow = head

        # Loop continues as long as the fast pointer can take 2 steps ahead
        while fast is not None and fast.next is not None:
            slow = slow.next       # Slow pointer moves 1 step at a time
            fast = fast.next.next  # Fast pointer moves 2 steps at a time

        # Since 'fast' moves twice as fast as 'slow', by the time 'fast' 
        # reaches the end of the list, 'slow' will be exactly in the middle.
        return slow
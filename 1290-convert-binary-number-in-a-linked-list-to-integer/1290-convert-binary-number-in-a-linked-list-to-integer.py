# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        bi_str = ''
        current_node = head
        
        while current_node != None:
            bi_str += str(current_node.val)
            current_node = current_node.next
            
        return int(bi_str, 2)
            
            
        
        
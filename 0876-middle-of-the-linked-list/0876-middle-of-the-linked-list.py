# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = calc_length(head)
        
        if length % 2 == 0:
            mid = int(length/2)
        else:
            mid = int(length/2) + 1
            
        count = 1
        current_node = head
        
        while count != mid:
            current_node = current_node.next
            count += 1
            
        return current_node
    
def calc_length(head):
    current_node = head
    length = 1

    while current_node != None:
        length +=1
        current_node = current_node.next

    return length
    
    
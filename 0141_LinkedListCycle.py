# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        indexes =[]
        current = head
        if current is None:
            return False
        while current.next:
            current = current.next
            print("current:", current)
            if current.next is None:
                return False
            indexes.append(current)
            for item in indexes:
                if item == current:
                    return True
        return False

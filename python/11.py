class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head  # 定义快慢指针
        
        while fast and fast.next:  # 只要快指针不为空，并且能向前走两步
            slow = slow.next       # 慢指针每次走一步
            fast = fast.next.next  # 快指针每次走两步
            
            if slow == fast:       # 如果快慢指针相遇，说明有环
                return True
        
        return False  # 如果快指针到达链表尾部，说明无环

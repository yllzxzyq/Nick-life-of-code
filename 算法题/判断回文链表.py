class Solution(object):
    #方法一，转成顺序表操作（利用栈，反转链表）
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        import copy
        h = head
        l = []
        while h:
            l.append(h.val)
            h = h.next
        l_re = copy.copy(l)
        l_re.reverse()
        return l==l_re
    #方法二，快慢指针，通过快慢指针找到中点位置，然后再反转链表
    def isPalindrome_fs(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        if fast:
            slow = slow.next
        while slow:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next

        cur = head
        while pre:
            if pre.val != cur.val:
                return False
            pre = pre.next
            cur = cur.next
        return True

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
head.next.next.next = ListNode(1)
s = Solution()
print(s.isPalindrome_fs(head))

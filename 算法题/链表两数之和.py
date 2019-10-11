class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    re = ListNode(0)
    r = re
    target = 0
    while l1 and l2:
        s = l1.val + l2.val + target
        r.next = ListNode(s % 10)
        r = r.next
        target = s // 10
        l1 = l1.next
        l2 = l2.next
    while not l1 and l2:
        s = l2.val + target
        r.next = ListNode(s % 10)
        r = r.next
        target = s // 10
        l2 = l2.next
    while l1 and not l2:
        s = l1.val + target
        r.next = ListNode(s % 10)
        r = r.next
        target = s // 10
        l1 = l1.next
    if target == 1:
        r.next = ListNode(1)
    return re.next

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


def getIntersectionNode(headA, headB):
    ha = headA
    hb = headB
    while ha and hb:
        ha = ha.next
        hb = hb.next
    stepa = 0
    while ha:
        stepa += 1
        ha = ha.next
    stepb = 0
    while hb:
        stepb += 1
        hb = hb.next

    starta = headA
    startb = headB
    a, b = 0, 0
    while a < stepa:
        a += 1
        starta = starta.next
    while b < stepb:
        b += 1
        startb = startb.next
    while starta != startb:
        if starta.next == None:
            return
        starta = starta.next
        startb = startb.next
    return starta
circle = ListNode(-1)
c=circle
for i in range(3):
    circle.next = ListNode(i)
    circle = circle.next
headA = ListNode('A')
headB = ListNode('B')
x=ListNode(-1)
headA.next = c
headB.next  = ListNode(-2)
headB.next.next = c
print(getIntersectionNode(headA, headB).val)
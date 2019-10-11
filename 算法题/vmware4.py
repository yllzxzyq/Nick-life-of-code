class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

str1,str2 = input().split(',')
k =str2.split('=')[-1]
L = str1.split('->')
n = len(L)
head = ListNode(0)
cur = head
for i in L:
    cur.next = ListNode(i)
    cur = cur.next
K = k%n
fast = head.next
slow = head.next
while K > 0:
    fast = fast.next
    K-=1
while fast.next:
    fast = fast.next
    slow = slow.next
fast.next = head.next
head.next = slow.next
slow.next = None
re = ''
c = head.next
while c.next:
    re += str(c.val)+'->'
    c = c.next
re +='NULL'
print(re)
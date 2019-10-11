from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        d = deque()
        d.append(root)
        re = [str(root.val)]
        while d:
            x = d.popleft()
            if x.left:
                d.append(x.left)
                re.append(str(x.left.val))
            else:
                re.append('null')
            if x.right:
                d.append(x.right)
                re.append(str(x.right.val))
            else:
                re.append('null')
        data = ','.join(re)
        data = '[' + data + ']'
        return data

    def deserialize(self, data):
        if not data:
            return
        s = data[1:-1]
        l = s.split(',')
        l.reverse()
        root = TreeNode(l.pop())
        d = deque()
        d.append(root)
        while l:
            cur  = d.popleft()
            left = l.pop()
            if left != 'null':
                cur.left = TreeNode(int(left))
                d.append(cur.left)
            if l:
                right = l.pop()
                if right != 'null':
                    cur.right = TreeNode(int(right))
                    d.append(cur.right)
        return root

s =  "[1,2,3,null,null,4,5]"
C = Codec()
root = C.deserialize(s)
re = C.serialize(root)
print(re)
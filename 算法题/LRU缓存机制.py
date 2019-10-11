# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

#利用列表和字典两种数据结构，put和get复杂度O(n)
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.list = []
        self.key_value = {}
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.list:
            return -1
        else:
            self.list.remove(key)
            self.list.append(key)
            return self.key_value[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.list)<self.cap:
            if key not in self.list:
                self.list.append(key)
                self.key_value[key] = value
            else:
                self.list.remove(key)
                self.list.append(key)
                self.key_value[key] = value
        else:
            if key not in self.list:
                self.key_value.pop(self.list.pop(0))
                self.list.append(key)
                self.key_value[key] = value
            else:
                self.list.remove(key)
                self.list.append(key)
                self.key_value[key] = value

#利用双向链表和字典完成，put和get复杂度O(1)
class dNodelist():
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


class LRUCache_O1(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.cap = capacity
        self.head = dNodelist()
        self.tail = dNodelist()
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add(self, node):
        node.pre = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.pre = node

    def pop_tail(self):
        x = self.tail.pre
        self.remove(x)
        return x.key

    def move_to_head(self, node):
        self.remove(node)
        self.add(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        else:
            node = self.dict.get(key)
            self.move_to_head(node)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = dNodelist(key, value)
        if key not in self.dict:
            self.dict[key] = new_node
            self.add(new_node)
            if len(self.dict) > self.cap:
                last = self.pop_tail()
                self.dict.pop(last)
        else:
            node = self.dict.get(key)
            self.move_to_head(node)
            node.val = new_node.val

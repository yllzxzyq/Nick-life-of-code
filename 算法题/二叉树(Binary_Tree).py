import uuid
from random import sample

class Tree:
    #初始化函数
    def __init__(self,value, left =None, right =None):
        self.value = value
        self.left = left
        self.right = right
        #self.dot = Digraph(comment='Binary Tree')
    #先序遍历
    def preorder(self):

        if self.value:
            print(self.value,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.self.preorder()
    #中序遍历
    def midoder(self):

        if self.left:
            self.left.midoder()
        if self.value:
            print(self.value,end=' ')
        if self.right:
            self.right.self.midoder()
    #后序遍历
    #后序遍历
    def postorder(self):

        if self.left:
            self.left.postoder()
        if self.right:
            self.right.self.postoder()
        if self.value:
            print(self.value, end=' ')
    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None

        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order
    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.value is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

        # 二叉树的叶子节点
    #二叉树的叶子节点
    def leaves(self):

        if self.value is None:
            return None
        elif self.left is None and self.right is None:
            print(self.value, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()

node1=Tree(1)
node2=Tree(2)
node1.left=node2
node1.preorder()

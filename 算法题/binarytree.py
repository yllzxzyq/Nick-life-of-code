from binarytree import *

# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)
# Generate a random BST and return its root node
my_bst = bst(height=3, is_perfect=True)
# Generate a random max heap and return its root node
my_heap = heap(height=3, is_max=True, is_perfect=False)
# Pretty-print the trees in stdout
print(my_tree)
print(my_bst)
print(my_heap)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
print(root)
root.properties  # To see all at once:

root = Node(1)                  # index: 0, value: 1
root.left = Node(2)             # index: 1, value: 2
root.right = Node(3)            # index: 2, value: 3
root.left.right = Node(4)       # index: 4, value: 4
root.left.right.left = Node(5)  # index: 9, value: 5

print(root)
#
#      ____1
#     /     \
#    2__     3
#       \
#        4
#       /
#      5

 # Use binarytree.Node.pprint instead of print to display indexes
root.pprint(index=True)
#
#       _________0-1_
#      /             \
#    1-2_____        2-3
#            \
#           _4-4
#          /
#        9-5
#
# Return the node/subtree at index 9
root[9]
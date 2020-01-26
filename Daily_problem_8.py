class Node:
    def __init__(self,data,left=None,right=None):
        self.value = data
        self.left = left
        self.right = right




def count_univals(root):
    total_count, is_unival = helper(root)
    return total_count


def helper(root):
    if root == None : return (0, True)
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if root.left != None and root.left.value != root.value:
        is_unival = False
    if root.right != None and root.right.value != root.value:
        is_unival = False
    if is_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)



node_right_left1 = Node(1, Node(1), Node(1))
node_right1 = Node(0, node_right_left1, Node(0))
tree1 = Node(0, Node(1), node_right1)
# tree1 looks like:
#         0
#        / \
#       1   0
#          / \
#         1   0
#        / \
#       1   1

node_right_right2 = Node(4, None, Node(4))
node_right2 = Node(4, Node(4), node_right_right2)
tree2 = Node(3, Node(2), node_right2)
# tree2 looks like:
#         3
#        / \
#       2   4
#          / \
#         4   4
#              \
#               4

node_right_right3 = Node(3, None, Node(2))
node_right3 = Node(3, Node(3), node_right_right3)
tree3 = Node(3, Node(3), node_right3)
# tree3 looks like:
#         3
#        / \
#       3   3
#          / \
#         3   3
#              \
#               2

# A function for going through the tree in order.
# Use this to test if we got the right tree.
def in_order(root):
    if root.left:
        in_order(root.left)
    print(str(root.value) + ', ', end='')
    if root.right:
        in_order(root.right)

in_order(tree1)
print('')
in_order(tree2)
print('')
in_order(tree3)
print('')


print(count_univals(tree1), 'should be 5')
print(count_univals(tree2), 'should be 5')
print(count_univals(tree3), 'should be 3')
print(count_univals(None), 'should be 0')

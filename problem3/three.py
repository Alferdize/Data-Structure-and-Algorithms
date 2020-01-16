class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    data = root.val
    if root.left != None:
        data += '-' + serialize(root.left)
    if root.right != None:
        data += '-' + serialize(root.right)
    return data


def deserialize(tree_string):
    tree_data = tree_string.split("-")
    node = decode(tree_data)
    return node

def decode(tree_data):
    node = Node(None)
    if len(tree_data) != 0:
        node.val = tree_data.pop(0)
        node.left = decode(tree_data)
        node.right = decode(tree_data)
    return node

node = Node('root', Node('left', Node('left.left'), Node('right.right')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


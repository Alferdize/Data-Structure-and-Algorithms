"""
one.py
"""

class Node:
    def __init__(self, val,left=None, right=None):
        self.val = val
        self.left = left
        self.right= right



def serialize(root):
    data = root.val
    if root.left != None:
        data = data + "-" + serialize(root.left)
    if root.right !=None:
        data = data + "-" + serialize(root.right)
    return data

def rebuild(tree_list):
    node = Node(None)

    if len(tree_list) != 0:
        value = tree_list.pop(0)
        node = Node(value)
        node.left = rebuild(tree_list)
        node.right = rebuild(tree_list)

    return node

def deserialize(treedata):
    tree_list = treedata.split('-')
    tree = rebuild(tree_list)
    return tree




node = Node('root', Node('left', Node('left.left'), Node('right.right')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

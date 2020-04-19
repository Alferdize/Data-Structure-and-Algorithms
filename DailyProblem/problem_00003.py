import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

def serialize(root):
    if not root:
        return None
    tree = dict()
    tree_left = serialize(root.left)
    tree_right = serialize(root.right)
    tree['data'] = root.data

    if tree_left:
        tree['left'] = tree_left
    if tree_right:
        tree['right'] = tree_right

    return json.dumps(tree)

def deserialize(s):
    tree = json.loads(s)

    node = Node(tree['data'])
    if 'left' in tree:
        node.left = deserialize(tree['left'])
    if 'right' in tree:
        node.right = deserialize(tree['right'])

    return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.data == 'left.left'
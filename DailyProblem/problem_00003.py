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

    serialize_tree_map = dict()
    serialize_left = serialize(root.left)
    serialize_right = serialize(root.right)
    serialize_tree_map['data'] = root.data
    print(serialize_tree_map)
    if serialize_left:
        serialize_tree_map['left'] = serialize_left
    if serialize_right:
        serialize_tree_map['right'] = serialize_right
    

    return json.dumps(serialize_tree_map)

def deserialize(s):
    serialize_tree_map = json.loads(s)
    print(serialize_tree_map)
    node = Node(serialize_tree_map['data'])
    if 'left' in serialize_tree_map:
        node.left = deserialize(serialize_tree_map['left'])
    if 'right' in serialize_tree_map:
        node.right = deserialize(serialize_tree_map['right'])
    
    return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.data == 'left.left'
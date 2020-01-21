class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root != None:
        data = root.val
    if root.left != None:
        data += "-" + serialize(root.left)
    if root.right != None:
        data += "-" + serialize(root.right)
    return data

def deserialize(treestring):
    tree_data = treestring.split("-")
    return decode(tree_data)

def decode(data):
    node = Node(None)
    if len(data) > 0:
        val = data.pop(0)
        node.val = val
        node.left = decode(data)
        node.right = decode(data)
    return node

node = Node('root', Node('left', Node('left.left'), Node('right.right')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
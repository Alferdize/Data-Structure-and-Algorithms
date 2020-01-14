"""
Daily_problem_3.py
Google Tree Problem
"""
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    data = root.val
    if root.left != None:
        data = data + "-" +  serialize(root.left)
    if root.right != None:
        data =  data + "-" + serialize(root.right)
    return data


# def serialize(root):
#         vals = []
#         def encode(node):
#             if node:
#                 vals.append(node.val)
#                 encode(node.left)
#                 encode(node.right)
#             else:
#                 vals.append('#')
        
#         encode(root)
        
#         return ' '.join(vals)


def deserialize(data):
    
    vals = deque(data.split('-'))
    return queue(vals)

def queue(data):
    val = data.popleft()
    print(val)
    if len(data) > 0 :
        queue(data)
        return val
    return 1
    


node = Node('root', Node('left', Node('left.left'), Node('right.right')), Node('right'))
data = serialize(node)
print(data)
# data.split("-")
assert deserialize(serialize(node)).left.left.val == 'left.left'

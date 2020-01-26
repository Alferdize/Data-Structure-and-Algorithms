class Node:
<<<<<<< HEAD
    def __init__(self,data):
        self.data = data
        self.both =  id(data)
=======
    def __init__(self, data):
        self.data = data
        self.both = id(data)
>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296

    def __repr__(self):
        return str(self.data)


<<<<<<< HEAD

=======
>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

id_map = dict()
id_map[id("a")] = a
id_map[id("b")] = b
id_map[id("c")] = c
id_map[id("d")] = d
id_map[id("e")] = e

<<<<<<< HEAD
class LinkedList:
    def __init__(self,node):
=======

class LinkedList:
    def __init__(self, node):
>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

<<<<<<< HEAD
    def add(self,element):
=======
    def add(self, element):
>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296
        self.tail.both ^= id(element.data)
        element.both = id(self.tail.data)
        self.tail = element

<<<<<<< HEAD
    def get(self,index):
        prev_node_element = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_element ^ result_node.both
            prev_node_element = id(result_node.data)
            result_node = id_map[next_node_address]
        return result_node.data

=======
    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.data)
            result_node = id_map[next_node_address]
        return result_node.data


>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296
llist = LinkedList(c)
llist.add(d)
llist.add(e)
llist.add(a)

assert llist.get(0) == "c"
assert llist.get(1) == "d"
assert llist.get(2) == "e"
<<<<<<< HEAD
assert llist.get(3) == "a"
=======
assert llist.get(3) == "a"
>>>>>>> 1062006ec8eee226c85e27c42a3b01491b27e296

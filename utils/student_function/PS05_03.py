from PS05 import *

def clone_node(node):
    r = None if node is None else Node(node.value,clone_node(node.next))
    return r

class Node:
    def __init__(self, value, parent, key):
        self.value = value
        self.parent_node = parent
        self.key = key
        self.is_taken = False
        self.left_child = None
        self.right_child = None

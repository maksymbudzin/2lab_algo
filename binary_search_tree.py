class BinaryTree:
    from node import Node

    def __init__(self, key, *value):
        self.key = key
        self.root_node = None

        if len(value) > 0:
            for value in value:
                self.add_elem(value)

    def add_elem(self, new_value):
        current_node = self.root_node

        if self.root_node is None:
            self.root_node = self.Node(new_value, parent=None, key=self.key(new_value))
            return

        while True:

            if self.key(current_node.value) < self.key(new_value):
                if current_node.right_child is None:
                    current_node.right_child = self.Node(new_value, parent=current_node,
                                                     key=self.key(new_value))
                    return
                else:
                    current_node = current_node.right_child
            elif self.key(current_node.value) > self.key(new_value):
                if current_node.left_child is None:
                    current_node.left_child = self.Node(new_value, parent=current_node,
                                                    key=self.key(new_value))
                    return
                else:
                    current_node = current_node.left_child
            else:
                current_node.value = new_value
                return

    def remove_elem(self):
        min_element = self.get_min_elem()
        if min_element.right_child is not None:
            if min_element.parent_node is None:
                min_element.right_child.parent_node = None
                self.root_node = min_element.right_child
            else:
                min_element.parent_node.left_child = min_element.right_child
        else:
            if min_element.parent_node is not None:
                min_element.parent_node.left_child = None
            else:
                self.root_node = None

    def get_max_elem(self):
        if self.root_node is not None:
            cur_node = self.root_node
            while cur_node.right_child is not None:
                cur_node = cur_node.right_child

            return cur_node

    def get_min_elem(self):
        if self.root_node is not None:
            cur_node = self.root_node
            while cur_node.left_child is not None:
                cur_node = cur_node.left_child

            return cur_node

    def get_min_value(self):
        return self.get_min_elem().value

    def get_max_value(self):
        return self.get_max_elem().value



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, key):
        self.head = None
        self.key = key

    def get_element(self, index):
        current = self.head
        if current is None: return
        for i in range(index):
            current = current.next
        return current.data

    def append(self, new_value):

        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def sorted_merge(self, left_part, right_part):
        result = None

        if left_part == None:
            return right_part
        if right_part == None:
            return left_part

        if self.key(left_part.data) <= self.key(right_part.data):
            result = left_part
            result.next = self.sorted_merge(left_part.next, right_part)
        else:
            result = right_part
            result.next = self.sorted_merge(left_part, right_part.next)

        return result

    def merge_sort(self, head):

        if head == None or head.next == None:
            return head

        middle = self.get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)

        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

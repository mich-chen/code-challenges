class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(node.data)

        node = node.next


def reverse(head):

    # if empty dll
    if head is None:
        return None

    # if only 1 node
    if head.next is None:
        return head

    current = head.next
    # store old head as new tail
    tail = head
    tail.next = None

    # traverse dll
    while current:
        # store current node's next for updating without misassigning other attributes
        next_node = current.next
        # set previous as current's next (reversing)
        current.prev = next_node
        # set current node to new reversed tail
        current.next = tail
        # update new reversed tail
        tail = current
        # update current to traverse backwards
        current = next_node

    return tail


if __name__ == '__main__':

# ***** test 1 *****
    for t_itr in range(1):
        llist_count = [1, 2, 3, 4]

        llist = DoublyLinkedList()

        for item in llist_count:
            llist.insert_node(item)

        llist1 = reverse(llist.head)
        print_doubly_linked_list(llist1)  # 4 3 2 1

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


def sortedInsert(head, data):

    new = DoublyLinkedListNode(data)

    # insert in empty list
    if head == None:
        return new

    # insert at beginning of list
    if head.data > data:
        new.next = head
        head.prev = new
        return new  # new head pointer of ll

    current = head

    while current:
        # if at tail of ll
        if current.next == None and current.data <= data:
            current.next = new
            new.prev = current
            break

        # if inserting in middle of ll
        # if current node is greater than data, then update current's prev's next as new
        if current.data >= data:
            prev = current.prev
            prev.next = current.prev = new
            new.prev = prev
            new.next = current
            break

        current = current.next
    
    return head


if __name__ == '__main__':

# ***** test 1 *****
    for t_itr in range(1):
        llist_count = [1, 3, 4, 10]

        llist = DoublyLinkedList()

        for item in llist_count:
            llist.insert_node(item)

        data = 5

        llist1 = sortedInsert(llist.head, data)
        print_doubly_linked_list(llist1)  # 1 3 4 5 10


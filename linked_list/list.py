
class Node(object):
    __slots__ = ["data", "next"]
    def __init__(self, d):
        self.next = None
        self.data = d
# end of class Node


class LinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            # end of while
            cur.next = new_node
        # end of if else
    # end of push

    def len(self):
        if self.head is None:
            return 0
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        # end of while
        return count

# end of linked List


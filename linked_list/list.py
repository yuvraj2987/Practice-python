
class Node(object):

    def __init__(self, d):
        self.next = None
        self.data = d

    def __repr__(self):
        return "Node({0.data!r})".format(self)

    def __str__(self):
        return "{0.data!s}".format(self)
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

    def __repr__(self):
        return "<LinkedList.head={0.head!r}>".format(self.head)

    def __str__(self):
        cur = self.head
        data_list = []
        while cur is not None:
            data_list.append(cur.data)
            cur = cur.next
        # end of while
        list_str = ", ".join(map(str, data_list))
        return "[{0!s}]".format(list_str)

# end of linked List


def main():
    l1 = LinkedList()
    print ("Emtpty list:")
    print(l1)
    l1.push(1)
    l1.push(2)
    l1.push(3)
    print ("3 node list:")
    print(l1)


if __name__ == '__main__':
    main()

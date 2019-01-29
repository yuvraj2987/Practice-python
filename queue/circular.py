#! /usr/bin/env python


class CircularQueue(object):
    """
    Circular Queue implementation using list in python
    """

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Invalid queue size")
        self._size = size
        self._array = [None] * size
        self._head = self._tail = -1

    def __next(self, cur_idx):
        """
        Returns next value index in circular queue
        :type cur_idx: int
        :rtype: int
        """
        if cur_idx == self._size - 1:
            return 0
        return cur_idx + 1

    def isEmpty(self):
        """
        Returns True if queue is empty
        :rtype: bool
        """
        return self._head == self._tail == -1

    def isFull(self):
        """
        Returns True if queue is full
        :rtype: bool
        """
        return self.__next(self._tail) == self._head

    def enQueue(self, value):
        """
        Adds value to the queue. Returns True/False to show success
        :type: value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        nt = self.__next(self._tail)
        self._array[nt] = value
        self._tail = nt
        if self._head < 0:
            self._head = self._tail
        return True

    def deQueue(self):
        """
        Removes the first element
        :type: value: int
        :rtype: bool
        """
        if self.isEmpty():
            return False
        # If queue has single element
        if self._head == self._tail:
            # reset
            self._array[self._tail] = None
            self._head = self._tail = -1

        else:
            self._array[self._head] = None
            self._head = self.__next(self._head)
        # end of if else
        return True

    def Front(self):
        """
        Return first item in the list
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self._array[self._head]


    def Rear(self):
        """
        Returns last item in the queue
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self._array[self._tail]

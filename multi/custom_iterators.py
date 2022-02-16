#! /usr/bin/env python

class EvenNumbers:
    last = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last += 2
        if self.last > 8:
            raise StopIteration
        # end of if
        return self.last

    def next(self):
        return self.__next__()

# end of EvenNumbers

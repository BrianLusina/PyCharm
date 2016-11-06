class Queue(object):
    def __init__(self):
        self._storage = {}
        self._start = -1
        self._end = -1

    def enqueue(self, val):
        self._end += 1
        self._storage[self._end] = val

    def dequeue(self):
        # check if there are values
        if self._end > self._start:
            next_up = self._storage[++self._start]
            del self._storage[self._start]
        return next_up

    def size(self):
        return self._end - self._start
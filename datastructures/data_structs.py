"""Simple data structures implemented in python"""


class Stack:
    """A python stack class"""

    def __init__(self):
        self.entries = []

    def push(self, entry):
        self.entries.append(entry)

    def pop(self):
        if len(self.entries) > 0:
            return self.entries.pop()

    def top(self):
        if len(self.entries) > 0:
            return self.entries[-1]

    def is_empty(self):
        return self.entries == []

    def size(self):
        return len(self.entries)


class Queue:
    """A python queue class"""

    def __init__(self):
        self.entries = []

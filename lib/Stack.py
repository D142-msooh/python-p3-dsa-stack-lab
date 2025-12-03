class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            items = []
        self.items = list(items)
        self.limit = limit
        self.added = len(self.items)

    def push(self, value):
        if self.limit is not None and self.added >= self.limit:
            raise OverflowError("Stack is full")
        
        self.items.append(value)
        self.added += 1

    def pop(self):
        if self.empty():
            return None
        self.added -= 1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def isEmpty(self):
        return self.empty()

    def full(self):
        if self.limit is None:
            return False
        return self.added >= self.limit

    def search(self, value):
        if value not in self.items:
            return -1
        
        index = self.items.index(value)
        
        return len(self.items) - index - 1
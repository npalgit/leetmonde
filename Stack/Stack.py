class Stack:
    def __init__(self):
        self.container = []
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            return self.container.pop()

    def push(self, item):
        self.length += 1
        self.container.append(item)
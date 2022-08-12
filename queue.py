
class MyQueue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek())

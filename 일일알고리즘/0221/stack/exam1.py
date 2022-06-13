# 스택
class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = [None] * self.size

    def is_empty(self):
        return True if self.top == -1 else False

    def is_full(self):
        return True if self.top == self.size - 1 else False

    def push(self, item):
        if self.is_full():
            raise Exception("It is full")
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise Exception('It is empty')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|   |' + result
            else:
                result = f'\n| {item} |' + result
        return result


my_stack = Stack(5)

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())

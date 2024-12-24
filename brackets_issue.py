class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)

    def clean(self):
        while not self.is_empty():
            self.pop()

    def is_sequence_correct(self, brackets: str):
        pairs = {'(': ')', '[': ']', '{': '}'}
        self.clean() # на случай, если до этого были некие взаимодействия с текущим стеком
        for char in brackets:
            if char in pairs.keys():
                self.push(char)
            elif char in pairs.values() and char == pairs[self.peek()]:
                self.pop()
        return self.is_empty()


stack = Stack()
print(stack.is_sequence_correct('([]{})'))
print(stack.is_sequence_correct('([)]'))
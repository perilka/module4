class Stack:
    def __init__(self): self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clean(self):
        while not self.is_empty():
            self.pop()



def calculate(token: str, a: int|float, b: int|float) -> int|float:
    if token == '+':
        return a + b
    elif token == '-':
        return b - a
    elif token == '*':
        return a * b
    else:
        return b / a


def is_number(i):
    try:
        float(i)
    except ValueError:
        return False
    else:
        return True


def rpn(lst: list[str|float|int]) -> int|float:
    stack = Stack()
    for token in lst:
        if is_number(token):
            stack.push(float(token))
        elif token in '+-*/':
            a = stack.pop()
            b = stack.pop()
            stack.push(calculate(token, a, b))
    return stack.peek()


print(rpn([3, 4, 2, '*', '+']))
print(rpn([7, 2, '/']))
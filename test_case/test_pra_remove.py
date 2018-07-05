def judge(expression):
    s = Stack()
    d = {'}':'{', '[':']', '(':')'}
    for i in expression:
        if i == '[' or i == '{' or i == '(':
            s.push(i)
        if i == ']' or i == '}' or i == ')':
            if s.is_empty():
                return False
            elif s.pop() != d[i]:
                return False
    if not s.is_empty():
        return False
    else:
        return True


class Stack(object):
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self.is_empty():
            raise ValueError
        return self._elems.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError
        return self._elems[-1]

if __name__ == "__main__":
    ep = "[a+b(5-4)]*{x+b+b*{(1+2})}"
    print(judge(ep))
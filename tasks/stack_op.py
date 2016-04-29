#!/usr/bin/python3


class ExtendedStack(list):
    def is_len_two(self):
        return len(self) >= 2
    def sum(self):
        if self.is_len_two():
            s = self.pop() + self.pop()
            self.append(s)

    def sub(self):
        if self.is_len_two():
            s = self.pop() - self.pop()
            self.append(s)

    def mul(self):
        if self.is_len_two():
            s = self.pop() * self.pop()
            self.append(s)

    def div(self):
        if self.is_len_two():
            s = self.pop() // self.pop()
            self.append(s)


# stack = ExtendedStack()
#
# stack.append(12)
# stack.append(13)
# print(stack)
# stack.div()
# print(stack)

# двусвязный список
class Node:
    def __init__(self, a):
        self.a = a
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
        self.imin = []

    # для стека
    def push(self, a):

        t = Node(a)
        if self.start is None:
            self.start = self.end = t
        else:
            self.start.prev = t
            t.next = self.start
            self.start = t
        self.size += 1

        if a is None:
            return
        if not self.imin or self.imin[-1] >= a:
            self.imin.append(a)

    def pop(self):
        if self.isempty():
            return None  # исключение добавить

        p = self.start.a
        if p == self.imin[-1]:
            self.imin.pop()

        self.start = self.start.next
        if self.start:
            self.start.prev = None
        else:
            self.end = None
        self.size -= 1
        return p

    def top(self):
        if self.start is None:
            return None  # исключение при пустом
        return self.start.a

    def mini(self):
        if self.start is None:
            return  # доделать исключения
        return self.imin[-1]

    #  для очереди и стека
    def isempty(self):
        return self.start is None

    def size_(self):
        return self.size

    # для очереди
    # def enqueue(self,a):
    #     t=Node(a)
    #     if self.start is None:
    #         self.start=self.end=t
    #     else:
    #         self.end.next=t
    #         t.prev=self.end
    #         self.end=t
    #     self.size+=1

    # def dequeue(self):
    #     if self.start is None:
    #         return # исключение добавить
    #     self.start=self.start.next
    #     if self.start:
    #         self.start.prev=None
    #     self.size-=1

    # def front(self):
    #     if self.start is None:
    #         return # исключение добавить
    #     return self.start.a

    # вывод
    def print_(self):
        t = self.start
        while t:
            print(t.a, end=" ")
            t = t.next


# очередь на стеках
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def enqueue(self, a):
        self.s1.push(a)
        self.size += 1

    def dequeue(self):
        if self.isempty():
            return  # ошибка
        if self.s2.isempty():
            while not self.s1.isempty():
                t = self.s1.pop()
                self.s2.push(t)
        self.size -= 1
        p = self.s2.pop()
        return p

    def front(self):
        if self.s1.isempty() and self.s2.isempty():
            return None  # error
        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
        return self.s2.top()

    def isempty(self):
        return self.s1.isempty() and self.s2.isempty()

    def size_(self):
        return self.size

    def print_(self):

        if self.isempty():
            return  # error

        elements = []

        if not self.s2.isempty():
            t = self.s2.start
            while t:
                elements.append(t.a)
                t = t.next

        if not self.s1.isempty():

            s1_elements = []
            t = self.s1.start
            while t:
                s1_elements.append(t.a)
                t = t.next
            elements.extend(s1_elements[::-1])

        print(" ".join(map(str, elements)))

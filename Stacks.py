class Stack(object):

    def __init__(self):
        self.alist = []

    def append(self, val):
        self.alist.append(val)

    def remove(self):
        if self.alist:
            self.alist.pop()
        else:
            return None

    def peek(self):
        if self.alist:
            return self.alist[-1]
        else:
            return None

    def __len__(self):
        return len(self.alist)

    def isEMpty(self):
        return self.alist == []

    def get_Stack(self):
        return self.alist

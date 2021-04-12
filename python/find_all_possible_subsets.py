class Stack:
    def __init__(self, array=None):
        if array is not None:
            self.stack = array
            self.length = len(array)
        else:
            self.stack = []
            self.length = 0
    
    def add(self, value):
        if value is not None:
            self.stack.append(value)
            self.length += 1
    
    def pop(self):
        if self.length != 0:
            self.length -= 1
            return self.stack.pop()
        return None

    def __str__(self):
        return str(self.stack)


def get_all_subsets(v, sets):
    l = len(v)

    if l == 0:
        return

    stack = Stack([-1])
    s = []

    while stack.length != 0:
        i = stack.pop() + 1

        while i < l:
            s.append(v[i])
            stack.add(i)
            i += 1

        if len(s) > 0:
            sets.append(s[:])
            s.pop()
    

if __name__ == "__main__":
    v = [1, 2, 3, 4]
    sets = []
    get_all_subsets(v, sets)
    print(sets)
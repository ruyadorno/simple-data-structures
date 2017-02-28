from linkedlist import LinkedListNode

class Stack:
    """Simple stack implementation"""

    def __init__(self, maxsize=-1):
        self._top = None
        self._size = 0
        self._maxsize = maxsize


    def push(self, value):
        """Push an item to the top of the stack in O(1)"""
        if self._size == self._maxsize:
            raise StackError('Stack is already full')

        self._size += 1
        self._top = LinkedListNode(value, self._top)


    def pop(self):
        """Pops the top item out of the stack in O(1)"""
        if self._size == 0:
            raise StackError('Stack is empty')

        self._size -= 1
        popping = self._top
        self._top = popping.next()
        popping.setNextNode(None)
        return popping.value


    def peek(self):
        """Access the value of top item without modifying the stack, O(1)"""
        return self._top.value


    def size(self):
        """Get the current stack size"""
        return self._size


class StackError(Exception):
    def __init__(self, msg):
        self.message = msg


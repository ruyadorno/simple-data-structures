class LinkedListNode():

    def __init__(self, value, next_node=None):
        self.value = value
        self._next_node = next_node


    def next(self):
        return self._next_node


    def setNextNode(self, next_node):
        self._next_node = next_node



class LinkedList():
    """Builds a LinkedList out of a list"""

    def __init__(self, from_list=[]):

        self.firstnode = None
        next = None

        for i in reversed(from_list):
            next = LinkedListNode(i, next)

        if next != None:
            self.firstnode = next


    def insertBetween(self, value, prev_node=None, next_node=None):
        newNode = LinkedListNode(value, next_node)

        if prev_node:
            prev_node.setNextNode(newNode)

        return newNode


    def insertBefore(self, value, node):

        if node == self.firstnode:
            return self.insertFirstNode(value)
        else:
            prev_node = self.firstnode
            while prev_node != None:
                if prev_node.next() == node:
                    break
                prev_node = prev_node.next()
            return self.insertBetween(value, prev_node, node)


    def insertAfter(self, value, node):
        return self.insertBetween(value, node, node.next())


    def insertFirstNode(self, value):
        self.firstnode = self.insertBetween(value, None, self.firstnode)
        return self.firstnode


    def items(self):
        """Returns an iterable for all the items in the list"""

        item = self.firstnode

        while item:
            yield item
            item = item.next()


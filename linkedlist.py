class LinkedListNode():

    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode


    def next(self):
        return self._nextnode


    def setNextNode(self, nextnode):
        self._nextnode = nextnode



class LinkedList():
    """Builds a LinkedList out of a list"""

    def __init__(self, from_list=[]):

        self.firstnode = None
        next = None

        for i in reversed(from_list):
            next = LinkedListNode(i, next)

        if next != None:
            self.firstnode = next


    def insertBetween(self, value, prev_node=None, nextnode=None):
        """Insert a node in between two given nodes, O(1)"""
        newnode = LinkedListNode(value, nextnode)

        if prev_node:
            prev_node.setNextNode(newnode)

        return newnode


    def insertBefore(self, value, node):
        """Insert value as the previous node just before a given node in O(n)"""
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
        """Insert value as the next node after a given node in O(1)"""
        return self.insertBetween(value, node, node.next())


    def insertFirstNode(self, value):
        """Insert value as first node of the linked list in O(1)"""
        self.firstnode = self.insertBetween(value, None, self.firstnode)
        return self.firstnode


    def insertLastNode(self, value):
        """Insert value as the last node of the linked list in O(n)"""
        lastnode = self.firstnode

        while lastnode.next():
            lastnode = lastnode.next()

        return self.insertBetween(value, lastnode, None)


    def removeNode(self, node):
        """Removes the given node in O(n)"""
        if node == self.firstnode:
            self.removeFirstNode()
        else:
            prev = self.firstnode
            next = node.next()
            while prev.next() != node:
                prev = prev.next()
            self.removeBetween(prev, next)


    def removeBetween(self, prev, next):
        """Removes a node in between two given nodes, O(1)"""
        if prev is None:
            return self.removeFirstNode()
        else:
            removednode = prev.next()
            removednode.setNextNode(None)
            prev.setNextNode(next)
            return removednode


    def removeBeforeNode(self, node):
        """Removes the node just before the given node in O(n)"""
        if node == self.firstnode:
            raise LinkedListError('Can not remove a node before firstnode')

        prev = None
        removednode = self.firstnode
        while removednode.next() != node:
            prev = removednode
            removednode = removednode.next()

        return self.removeBetween(prev, node)


    def removeFirstNode(self):
        """Removes the first node of the linked list, O(1)"""
        removednode = self.firstnode
        self.firstnode = self.firstnode.next()
        removednode.setNextNode(None)
        return removednode


    def removeLastNode(self):
        """Removes the last node of the linked list in O(n)"""
        prev = None
        lastnode = self.firstnode
        while lastnode:
            prev = lastnode
            lastnode = lastnode.next()

        if prev == self.firstnode:
            return self.removeFirstNode()
        else:
            prev.setNextNode(None)
            return lastnode


    def items(self):
        """Returns an iterable for all the items in the list"""

        item = self.firstnode

        while item:
            yield item
            item = item.next()


class LinkedListError(Exception):
    def __init__(self, msg):
        self.message = msg


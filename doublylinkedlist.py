class DoublyLinkedListNode:

    class SentinelNode:
        pass

    sentinel = SentinelNode()


    def __init__(self, value):
        self.value = value


    def next(self):
        if self._nextnode.value is DoublyLinkedListNode.sentinel:
            return None
        else:
            return self._nextnode


    def prev(self):
        if self._prevnode.value is DoublyLinkedListNode.sentinel:
            return None
        else:
            return self._prevnode


    def setNextNode(self, nextnode):
        self._nextnode = nextnode


    def setPrevNode(self, prevnode):
        self._prevnode = prevnode


class DoublyLinkedList:
    """Builds a DoublyLinkedList from a list and provides helper methods"""

    def __init__(self, from_list=[]):
        self.head = DoublyLinkedListNode(DoublyLinkedListNode.sentinel)
        self.tail = DoublyLinkedListNode(DoublyLinkedListNode.sentinel)
        self.head.setNextNode(self.tail)
        self.tail.setPrevNode(self.head)

        prev = self.head
        for i in from_list:
            newnode = DoublyLinkedListNode(i)
            newnode.setPrevNode(prev)
            prev.setNextNode(newnode)
            prev = newnode

        if prev:
            self.tail.setPrevNode(prev)
            prev.setNextNode(self.tail)


    def firstnode(self):
        """Gets the first node of the list in O(1)"""
        return self.head.next()


    def lastnode(self):
        """Gets the last node of the list in O(1)"""
        return self.tail.prev()


    def insertFirstNode(self, value):
        """Inserts a new node at the start of the list in O(1)"""
        self.insertAfter(value, self.head)


    def insertLastNode(self, value):
        """Inserts a new node at the end of the list in O(1)"""
        self.insertBefore(value, self.tail)


    def insertBefore(self, value, node):
        """Inserts a new node with value before the given node in O(1)"""
        newnode = DoublyLinkedListNode(value)
        newnode.setNextNode(node)
        prev = node._prevnode
        prev.setNextNode(newnode)
        node.setPrevNode(newnode)
        newnode.setPrevNode(prev)


    def insertAfter(self, value, node):
        """Inserts a new node with value after the given node in O(1)"""
        newnode = DoublyLinkedListNode(value)
        newnode.setPrevNode(node)
        next = node._nextnode
        next.setPrevNode(newnode)
        node.setNextNode(newnode)
        newnode.setNextNode(next)


    def removeNode(self, node):
        """Removes a node from the list in O(1)"""
        prev = node._prevnode
        next = node._nextnode
        prev.setNextNode(next)
        next.setPrevNode(prev)
        node.setNextNode(None)
        node.setPrevNode(None)
        return node


    def removeFirstNode(self):
        """Removes the first node of the list in O(1)"""
        if self.firstnode():
            return self.removeAfterNode(self.head)


    def removeLastNode(self):
        """Removes the last node of the list in O(1)"""
        if self.lastnode():
            return self.removeBeforeNode(self.tail)


    def removeBeforeNode(self, node):
        """Removes and returns the node just before the given node in O(1)"""
        if node._prevnode.value is DoublyLinkedListNode.sentinel:
            raise DoublyLinkedListError('Can\'t remove a node before firstnode')

        return self.removeNode(node._prevnode)


    def removeAfterNode(self, node):
        """Removes and returns the node just before the given node in O(1)"""
        if node._nextnode.value is DoublyLinkedListNode.sentinel:
            raise DoublyLinkedListError('Can\'t remove a node after lastnode')

        return self.removeNode(node._nextnode)


    def removeAllInBetween(self, fromnode, tonode):
        """Removes all nodes in between and returns a new linked list"""
        sliced_list = DoublyLinkedList()
        if fromnode.next() is tonode or tonode.prev() is fromnode:
            return sliced_list

        sliced_list.head.setNextNode(fromnode.next())
        sliced_list.tail.setPrevNode(tonode.prev())
        fromnode.next().setPrevNode(sliced_list.head)
        tonode.prev().setNextNode(sliced_list.tail)
        fromnode.setNextNode(tonode)
        tonode.setPrevNode(fromnode)
        return sliced_list


    def items(self):
        """Returns an iterable for all the items in the list"""

        item = self.firstnode()

        while item:
            yield item
            item = item.next()

class DoublyLinkedListError(Exception):
    def __init__(self, msg):
        self.message = msg


import unittest
from linkedlist import LinkedList, LinkedListNode

class TestLinkedList(unittest.TestCase):

    def test_create_new_linked_linked_list(self):
        linked_list = LinkedList()
        self.assertIsInstance(linked_list, LinkedList)

    def test_create_new_linked_list_from_list(self):
        linked_list = LinkedList([1])
        self.assertIsInstance(linked_list.firstnode, LinkedListNode)
        self.assertEqual(linked_list.firstnode.value, 1)

    def test_get_next_node(self):
        linked_list = LinkedList(['a', 'b'])
        self.assertEqual(linked_list.firstnode.next().value, 'b')

    def test_linked_list_items_iterator(self):
        linked_list = LinkedList([1, 2, 3])
        count = 0
        for i in linked_list.items():
            self.assertIsInstance(i, LinkedListNode)
            self.assertGreater(i.value, 0)
            count += 1
        self.assertEqual(count, 3)

    def test_insert_between(self):
        linked_list = LinkedList([1, 2])
        self.assertEqual(linked_list.firstnode.next().value, 2)
        linked_list.insertBetween(3, linked_list.firstnode, linked_list.firstnode.next())
        self.assertEqual(linked_list.firstnode.next().value, 3)

    def test_insert_after(self):
        linked_list = LinkedList([1, 2])
        self.assertEqual(linked_list.firstnode.next().value, 2)
        linked_list.insertAfter(3, linked_list.firstnode)
        self.assertEqual(linked_list.firstnode.next().value, 3)

    def test_insert_before(self):
        linked_list = LinkedList([1, 2])
        self.assertEqual(linked_list.firstnode.next().value, 2)
        linked_list.insertBefore(3, linked_list.firstnode.next())
        self.assertEqual(linked_list.firstnode.next().value, 3)

    def test_insert_before_first_node(self):
        linked_list = LinkedList([1, 2])
        self.assertEqual(linked_list.firstnode.value, 1)
        linked_list.insertBefore(3, linked_list.firstnode)
        self.assertEqual(linked_list.firstnode.value, 3)

    def test_build_list_dynamically(self):
        linked_list = LinkedList()
        linked_list.insertFirstNode(1)
        self.assertEqual(linked_list.firstnode.value, 1)
        linked_list.insertFirstNode(2)
        self.assertEqual(linked_list.firstnode.value, 2)
        linked_list.insertFirstNode(3)
        self.assertEqual(len([i for i in linked_list.items()]), 3)

    def test_insert_last_node(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.insertLastNode(4)
        self.assertEqual(linked_list.firstnode.next().next().next().value, 4)
        self.assertEqual(len([i for i in linked_list.items()]), 4)

    def test_remove_between_nodes(self):
        linked_list = LinkedList([1, 2, 3])
        prev_node = linked_list.firstnode
        next_node = linked_list.firstnode.next().next()
        removed = linked_list.removeBetween(prev_node, next_node)
        self.assertEqual(removed.value, 2)
        self.assertEqual(len([i for i in linked_list.items()]), 2)

    def test_remove_between_nodes_first_node(self):
        linked_list = LinkedList([1, 2])
        prev_node = None
        next_node = linked_list.firstnode.next()
        removed = linked_list.removeBetween(prev_node, next_node)
        self.assertEqual(removed.value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 1)

    def test_remove_node(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertEqual(len([i for i in linked_list.items()]), 3)
        remove_node = linked_list.firstnode.next()
        linked_list.removeNode(remove_node)
        self.assertEqual(len([i for i in linked_list.items()]), 2)

    def test_remove_before_node(self):
        linked_list = LinkedList([1, 2, 3])
        self.assertEqual(len([i for i in linked_list.items()]), 3)
        node = linked_list.firstnode.next().next()
        self.assertEqual(linked_list.removeBeforeNode(node).value, 2)
        node = linked_list.firstnode.next()
        self.assertEqual(linked_list.removeBeforeNode(node).value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 1)

    def test_remove_first_node(self):
        linked_list = LinkedList([1, 2, 3])
        removed = linked_list.removeFirstNode()
        self.assertEqual(removed.value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 2)

    def test_remove_first_node_single_item(self):
        linked_list = LinkedList([1])
        removed = linked_list.removeFirstNode()
        self.assertEqual(removed.value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 0)

    def test_remove_last_node(self):
        linked_list = LinkedList([1, 2, 3])
        removed = linked_list.removeFirstNode()
        self.assertEqual(removed.value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 2)

    def test_remove_last_node_single_item(self):
        linked_list = LinkedList([1])
        removed = linked_list.removeLastNode()
        self.assertEqual(removed.value, 1)
        self.assertEqual(len([i for i in linked_list.items()]), 0)


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
        for i in linked_list.items():
            self.assertIsInstance(i, LinkedListNode)
            self.assertGreater(i.value, 0)

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


import unittest
from doublylinkedlist import DoublyLinkedList, DoublyLinkedListNode, DoublyLinkedListError

class TestDoublyLinkedList(unittest.TestCase):

    def test_create_new_linked_list(self):
        dl_list = DoublyLinkedList()
        self.assertIsInstance(dl_list, DoublyLinkedList)

    def test_create_new_linked_list_from_list(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertIsInstance(dl_list, DoublyLinkedList)
        self.assertEqual(dl_list.firstnode().value, 1)
        self.assertEqual(dl_list.lastnode().value, 3)

    def test_create_new_linked_list_one_elem(self):
        dl_list = DoublyLinkedList([1])
        self.assertEqual(dl_list.firstnode().value, 1)
        self.assertEqual(dl_list.lastnode().value, 1)

    def test_sentinel_nodes_should_not_be_listed(self):
        dl_list = DoublyLinkedList([1])
        self.assertEqual(dl_list.firstnode().next(), None)
        self.assertEqual(dl_list.firstnode().prev(), None)

    def test_firstnode_on_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(dl_list.firstnode(), None)

    def test_lastnode_on_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(dl_list.lastnode(), None)

    def test_items_iterator(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        count = 0
        for i in dl_list.items():
            self.assertIsInstance(i, DoublyLinkedListNode)
            self.assertGreater(i.value, 0)
            count += 1
        self.assertEqual(count, 3)

    def test_insert_before(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertBefore(4, dl_list.lastnode().prev())
        self.assertEqual(dl_list.lastnode().prev().prev().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_insert_before_first_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertBefore(4, dl_list.firstnode())
        self.assertEqual(dl_list.firstnode().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_insert_after(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertAfter(4, dl_list.firstnode())
        self.assertEqual(dl_list.firstnode().next().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_insert_after_last_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertAfter(4, dl_list.lastnode())
        self.assertEqual(dl_list.lastnode().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_remove_node(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.removeNode(dl_list.lastnode().prev())
        self.assertEqual(dl_list.lastnode().prev().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_node_unique_item(self):
        dl_list = DoublyLinkedList([1])
        self.assertEqual(len([i for i in dl_list.items()]), 1)
        dl_list.removeNode(dl_list.firstnode())
        self.assertEqual(dl_list.firstnode(), None)
        self.assertEqual(len([i for i in dl_list.items()]), 0)

    def test_remove_node_first_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.removeNode(dl_list.firstnode())
        self.assertEqual(dl_list.firstnode().value, 2)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_node_last_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.removeNode(dl_list.lastnode())
        self.assertEqual(dl_list.lastnode().value, 2)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_before(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.removeBeforeNode(dl_list.lastnode())
        self.assertEqual(dl_list.lastnode().prev().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_before_first_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        with self.assertRaises(DoublyLinkedListError):
            dl_list.removeBeforeNode(dl_list.firstnode())

    def test_remove_after(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.removeAfterNode(dl_list.firstnode())
        self.assertEqual(dl_list.firstnode().next().value, 3)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_after_first_item(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        with self.assertRaises(DoublyLinkedListError):
            dl_list.removeAfterNode(dl_list.lastnode())

    def test_remove_all_in_between(self):
        dl_list = DoublyLinkedList([1, 2, 3, 4, 5, 6])
        self.assertEqual(len([i for i in dl_list.items()]), 6)
        new_list = dl_list.removeAllInBetween(\
            dl_list.firstnode().next(), dl_list.lastnode().prev())
        self.assertEqual(len([i for i in dl_list.items()]), 4)
        self.assertEqual(len([i for i in new_list.items()]), 2)
        self.assertEqual(new_list.firstnode().value, 3)

    def test_remove_all_in_between_single_item(self):
        dl_list = DoublyLinkedList([1, 2, 3, 4, 5, 6])
        self.assertEqual(len([i for i in dl_list.items()]), 6)
        new_list = dl_list.removeAllInBetween(\
            dl_list.firstnode(), dl_list.firstnode().next().next())
        self.assertEqual(len([i for i in dl_list.items()]), 5)
        self.assertEqual(len([i for i in new_list.items()]), 1)
        self.assertEqual(new_list.firstnode().value, 2)

    def test_remove_all_in_between_empty(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        new_list = dl_list.removeAllInBetween(\
            dl_list.firstnode(), dl_list.firstnode().next())
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        self.assertEqual(len([i for i in new_list.items()]), 0)
        self.assertEqual(new_list.firstnode(), None)

    def test_insert_first_node(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertFirstNode(4)
        self.assertEqual(dl_list.firstnode().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_insert_first_node_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(len([i for i in dl_list.items()]), 0)
        dl_list.insertFirstNode(1)
        self.assertEqual(dl_list.firstnode().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 1)

    def test_insert_last_node(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        dl_list.insertLastNode(4)
        self.assertEqual(dl_list.lastnode().value, 4)
        self.assertEqual(len([i for i in dl_list.items()]), 4)

    def test_insert_last_node_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(len([i for i in dl_list.items()]), 0)
        dl_list.insertLastNode(1)
        self.assertEqual(dl_list.lastnode().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 1)

    def test_remove_first_node(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        self.assertEqual(dl_list.removeFirstNode().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_first_node_single_item(self):
        dl_list = DoublyLinkedList([1])
        self.assertEqual(len([i for i in dl_list.items()]), 1)
        self.assertEqual(dl_list.removeFirstNode().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 0)

    def test_remove_first_node_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(len([i for i in dl_list.items()]), 0)
        self.assertEqual(dl_list.removeFirstNode(), None)
        self.assertEqual(len([i for i in dl_list.items()]), 0)

    def test_remove_last_node(self):
        dl_list = DoublyLinkedList([1, 2, 3])
        self.assertEqual(len([i for i in dl_list.items()]), 3)
        self.assertEqual(dl_list.removeLastNode().value, 3)
        self.assertEqual(len([i for i in dl_list.items()]), 2)

    def test_remove_last_node_single_item(self):
        dl_list = DoublyLinkedList([1])
        self.assertEqual(len([i for i in dl_list.items()]), 1)
        self.assertEqual(dl_list.removeLastNode().value, 1)
        self.assertEqual(len([i for i in dl_list.items()]), 0)

    def test_remove_last_node_empty_list(self):
        dl_list = DoublyLinkedList()
        self.assertEqual(len([i for i in dl_list.items()]), 0)
        self.assertEqual(dl_list.removeLastNode(), None)
        self.assertEqual(len([i for i in dl_list.items()]), 0)


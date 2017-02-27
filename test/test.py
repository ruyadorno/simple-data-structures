import unittest
from doublylinkedlist_test import TestDoublyLinkedList
from linkedlist_test import TestLinkedList

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDoublyLinkedList())
    suite.addTest(TestLinkedList())
    return suite


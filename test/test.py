import unittest
from doublylinkedlist_test import TestDoublyLinkedList
from linkedlist_test import TestLinkedList
from stack_test import TestStack

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDoublyLinkedList())
    suite.addTest(TestLinkedList())
    suite.addTest(TestStack())
    return suite


import unittest
from linkedlist_test import TestLinkedList

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestLinkedList())
    return suite


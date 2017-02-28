import unittest
from stack import Stack, StackError

class TestStack(unittest.TestCase):

    def test_create_new_stack(self):
        stack = Stack()
        self.assertIsInstance(stack, Stack)

    def test_empty_stack(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_push_item_increases_size(self):
        stack = Stack()
        stack.push('a')
        self.assertEqual(stack.size(), 1)

    def test_push_item_increases_size_more(self):
        stack = Stack()
        for i in list(range(100)):
            stack.push(i)
        self.assertEqual(stack.size(), 100)

    def test_peek_first_item(self):
        stack = Stack()
        stack.push('a')
        self.assertEqual(stack.peek(), 'a')

    def test_peek_first_item_more(self):
        stack = Stack()
        for i in list(range(100)):
            stack.push(i)
        self.assertEqual(stack.peek(), 99)

    def test_pop_item_decreases_size(self):
        stack = Stack()
        for i in list(range(100)):
            stack.push(i)
        self.assertEqual(stack.size(), 100)
        stack.pop()
        self.assertEqual(stack.size(), 99)

    def test_pop_item_returns_value(self):
        stack = Stack()
        for i in list(range(100)):
            stack.push(i)
        self.assertEqual(stack.pop(), 99)

    def test_pop_multiple_items(self):
        stack = Stack()
        for i in list(range(100)):
            stack.push(i)
        self.assertEqual(stack.pop(), 99)
        self.assertEqual(stack.pop(), 98)
        self.assertEqual(stack.pop(), 97)

    def test_push_and_pop(self):
        stack = Stack()
        stack.push('a')
        self.assertEqual(stack.peek(), 'a')
        stack.push('b')
        stack.push('c')
        stack.push('d')
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 'd')
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.pop(), 'd')
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), 'c')
        self.assertEqual(stack.size(), 2)
        stack.push('C')
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 'C')
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), 'C')
        self.assertEqual(stack.size(), 2)
        stack.push('D')
        self.assertEqual(stack.size(), 3)
        stack.push('E')
        self.assertEqual(stack.size(), 4)
        self.assertEqual(stack.peek(), 'E')
        self.assertEqual(stack.size(), 4)

    def test_below_maxsize(self):
        stack = Stack(10)
        stack.push('a')
        stack.push('b')
        stack.push('c')
        self.assertEqual(stack.size(), 3)

    def test_above_maxsize(self):
        stack = Stack(2)
        stack.push('a')
        stack.push('b')
        with self.assertRaises(StackError):
            stack.push('c')

    def test_pop_from_empty_stack(self):
        stack = Stack()
        with self.assertRaises(StackError):
            stack.pop()


import unittest as test
from descending_order import descending_order

try:
    desc_order = descending_order
except NameError:
    print("Name error encountered..")


class FixedTest(test.TestCase):
    def test_desc(self):

        self.assertEqual(desc_order(1), 1)
        self.assertEqual(desc_order(123), 321)
        self.assertEqual(desc_order(1021), 2110)
        self.assertEqual(desc_order(123456789), 98764321)


import unittest


def add(a, b):
    return a * b


class TestAdd(unittest.TestCase):
    def test_add_positive_nums(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()

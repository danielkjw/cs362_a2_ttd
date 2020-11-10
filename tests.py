import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1_init_test(self):
        input = 1
        expected = '1'
        self.assertFalse(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()


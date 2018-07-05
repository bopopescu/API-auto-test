import unittest
import os

class TestOne(unittest.TestCase):
    def setUp(self):
        print '\ncases before'
        pass

    def test_add(self):
        print 'add:'
        a = 3 + 4
        b = 7
        self.assertEqual(a,b)

    def test_sub(self):
        print 'sub:'
        a = 10 - 5
        b = 5
        self.assertEqual(a,b)

    def tearDown(self):
        print 'after'
        pass

if __name__ == '__main__':
    test_dir = os_path.join(os.getcwd())

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner

    runner.run(discover)
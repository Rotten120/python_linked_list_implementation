import unittest
from von_lab4 import *

class TestRemoveBeginning(unittest.TestCase):
    def setup(self, size):
        arr = LinkedList()
        for i in range(size):
            arr.insert_at_end(i)
        return arr

    def exe_test(self, size, rm_ele = None, new_arr = []):
        arr = self.setup(size)
        self.assertEqual(arr.remove_beginning(), rm_ele)
        self.assertEqual(list(arr), new_arr)
    
    def test_empty(self):
        self.exe_test(0)
        
    def test_one(self):
        self.exe_test(1, 0, [])
        
    def test_two(self):
        self.exe_test(2, 0, [1])

    def test_three(self):
        self.exe_test(3, 0, [1, 2])

class TestRemoveEnd(unittest.TestCase):
    def setup(self, size):
        arr = LinkedList()
        for i in range(size):
            arr.insert_at_end(i)
        return arr

    def exe_test(self, size, rm_ele = None, new_arr = []):
        arr = self.setup(size)
        self.assertEqual(arr.remove_at_end(), rm_ele)
        self.assertEqual(list(arr), new_arr)
        
    def test_empty(self):
        self.exe_test(0)

    def test_one(self):
        self.exe_test(1, 0, [])

    def test_two(self):
        self.exe_test(2, 1, [0])

    def test_three(self):
        self.exe_test(3, 2, [0, 1])

class TestRemoveAt(unittest.TestCase):
    def setup(self, size):
        arr = LinkedList()
        for i in range(size):
            arr.insert_at_end(i)
        return arr

    def exe_test(self, size, data, rm_ele = None, new_arr = []):
        arr = self.setup(size)
        self.assertEqual(arr.remove_at(data), rm_ele)
        self.assertEqual(list(arr), new_arr)

    def test_empty(self):
        self.exe_test(0, 1)

    def test_one(self):
        self.exe_test(1, 0, 0)

    def test_data_not_in_arr(self):
        self.exe_test(10, 123, None, list(range(10)))

    def test_data_in_arr(self):
        self.exe_test(5, 3, 3, [0, 1, 2, 4])

    def test_data_in_begin(self):
        self.exe_test(3, 0, 0, [1, 2])

if __name__ == "__main__":
    unittest.main()

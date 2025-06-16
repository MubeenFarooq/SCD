import unittest
import os
from stats import FileStats

class TestFileStats(unittest.TestCase):
    
    def setUp(self):
        # Create a test file with valid numbers
        with open('test_valid.txt', 'w') as f:
            f.write('10\n20\n30\n40\n50\n')
            
        # Create a test file with mixed valid and invalid data
        with open('test_mixed.txt', 'w') as f:
            f.write('10\nabc\n20\n30.5\ninvalid\n')
            
        # Create an empty file
        with open('test_empty.txt', 'w') as f:
            f.write('')
    
    def tearDown(self):
        test_files = ['test_valid.txt', 'test_mixed.txt', 'test_empty.txt']
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
    
    def test_valid_file_reading(self):
        """Test reading a file with valid numbers."""
        stats = FileStats('test_valid.txt')
        self.assertTrue(stats.read_file())
        self.assertEqual(len(stats.values), 5)
        self.assertEqual(stats.values, [10, 20, 30, 40, 50])
    
    def test_mixed_file_reading(self):
        stats = FileStats('test_mixed.txt')
        self.assertTrue(stats.read_file())
        self.assertEqual(len(stats.values), 4)
        self.assertEqual(stats.values, [10, 20, 30.5])
    
    def test_empty_file(self):
        stats = FileStats('test_empty.txt')
        self.assertFalse(stats.read_file())
    
    def test_nonexistent_file(self):
        
        stats = FileStats('nonexistent.txt')
        self.assertFalse(stats.read_file())
    
    def test_statistics_calculation(self):
        
        stats = FileStats('test_valid.txt')
        stats.read_file()
        result = stats.calculate_stats()
        
        self.assertIsNotNone(result)
        self.assertEqual(result['sum'], 150)
        self.assertEqual(result['average'], 30)
        self.assertEqual(result['minimum'], 10)
        self.assertEqual(result['maximum'], 50)
    
    def test_empty_statistics(self):
        
        stats = FileStats('test_empty.txt')
        stats.read_file()
        result = stats.calculate_stats()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 
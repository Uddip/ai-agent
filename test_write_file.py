import unittest
from functions.write_file import write_file

def TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_write_existing_file(self):


    def test_write_new_file(self):


    def test_write_error_outside_working_directory(self):

if __name__ == "__main__":
    unittest.main()

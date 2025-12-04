import os
import unittest
import config
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def assertContainsAll(self, text, substrings):
    for substring in substrings:
        self.assertIn(substring, text)

    def setUp(self):
        self.working_directory = os.getcwd()

    def test_lorem_truncate(self):
        expected_len = MAX_CHARS + len(TRUNC_MESSAGE)
        result = get_file_content("calculator", "lorem.txt")
        self.assertEqual

if __name__ == "__main__":
    unittest.main()


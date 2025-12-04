import os
import unittest
from functions.get_file_content import get_file_content
from config import MAX_CHARS, trunc_message

class TestGetFileContent(unittest.TestCase):

    def assertContainsAll(self, text, substrings):
        for substring in substrings:
            self.assertIn(substring, text)

    def setUp(self):
#        self.working_directory = os.getcwd()
        self.working_directory = "calculator"

    def test_lorem_truncate(self):
        file_path = "lorem.txt"
        expected_len = MAX_CHARS + len(trunc_message(file_path))
        result = get_file_content(self.working_directory, file_path)
        print(f"LEN: {len(result)}")
        print(f"END OF RES: {repr(result[10001:])}\nTRUNC STRING: {repr(trunc_message(file_path))}")
        self.assertEqual(len(result), expected_len)

        self.assertIn(trunc_message(file_path), result[10001:])

if __name__ == "__main__":
    unittest.main()


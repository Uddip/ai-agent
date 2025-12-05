import os
import unittest
from functions.get_file_content import get_file_content
from config import MAX_CHARS, trunc_message

class TestGetFileContent(unittest.TestCase):

    def assertContainsAll(self, text, substrings):
        for substring in substrings:
            self.assertIn(substring, text)

    def setUp(self):
        self.working_directory = "calculator"

    def test_lorem_string_truncated(self):
        file_path = "lorem.txt"
        expected_len = MAX_CHARS + len(trunc_message(file_path))
        result = get_file_content(self.working_directory, file_path)

        self.assertEqual(len(result), expected_len)
        self.assertIn(trunc_message(file_path), result[10000:])
        print(result)

    def test_main_py_content(self):
        file_path = "main.py"
        expected = "def main():"

        result = get_file_content(self.working_directory, file_path)
        self.assertIn(expected, result)
        print(result)

    def test_calculator_py_content(self):
        file_path = "pkg/calculator.py"
        expected = "def _apply_operator(self, operators, values)"

        result = get_file_content(self.working_directory, file_path)
        self.assertIn(expected, result)
        print(result)


    def test_file_outside_working_directory(self):
        file_path = "/bin/cat"
        expected = f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

        result = get_file_content(self.working_directory, file_path)
        self.assertEqual(result, expected)
        print(result)


    def test_non_existent_file(self):
        file_path = "pkg/does_not_exist.py"
        expected = f"Error: File not found or is not a regular file: \"{file_path}\" "

        result = get_file_content(self.working_directory, file_path)
        self.assertEqual(result, expected)
        print(result)


if __name__ == "__main__":
    unittest.main()


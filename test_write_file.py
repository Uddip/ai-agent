import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_write_existing_file(self):
        file_path = "lorem.txt"
        content = "wait, this isn't lorem ipsum"
        expected = "28 characters written"

        result = write_file(self.working_directory, file_path, content)

        self.assertIn(expected, result)
        print(result)

    def test_write_new_file(self):
        file_path = "pkg/morelorem.txt"
        content = "lorem ipsum dolor sit amet"
        expected = "26 characters written"

        result = write_file(self.working_directory, file_path, content)

        self.assertIn(expected, result)
        print(result)

    def test_write_error_outside_working_directory(self):
        file_path = "/tmp/temp.txt"
        content = "this should not be allowed"
        expected = "Error:"

        result = write_file(self.working_directory, file_path, content)

        self.assertIn(expected, result)
        print(result)


if __name__ == "__main__":
    unittest.main()

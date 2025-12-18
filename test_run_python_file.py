import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_print_usage_instructions_for_calculator(self):
        file_path = "main.py"
        expected = 'Usage: python main.py "<expression>"'

        result = run_python_file(self.working_directory, file_path)

        self.assertEqual(expected, result)
        print(result)

    def test_run_calculator(self):
        file_path = "main.py"
        args = ["3 + 5"]
        expected = '8'

        result = run_python_file(self.working_directory, file_path, args)

        self.assertIn(expected, result)
        print(result)

    def test_run_calculator_tests(self):

    def test_run_python_file_to_error_outside_working_dir(self):

    def test_run_python_file_to_error_nonexistent_file(self):

    def test_run_python_file_to_error_not_py_file(self):

if __name__ == "__main__":
    unittest.main()

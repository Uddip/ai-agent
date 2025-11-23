import os
import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def assertContainsAll(self, text, substrings):
      for substring in substrings:
        self.assertIn(substring, text)

    def setUp(self):
      self.working_directory = os.getcwd()

    def test_calculator_directory(self):
      expected = [
        "Result for current directory",
        "main.py",
        "tests.py",
        "pkg",
        "is_dir=",
        "file_size="
      ]
      
      result = get_files_info("calculator", ".")
      self.assertContainsAll(result, expected)
      print(result)
    
    def test_pkg_directory_in_calculator(self):
      expected = [
        "Result for 'pkg' directory",
        "calculator.py",
        "render.py",
        "is_dir=",
        "file_size="
      ]

      result = get_files_info("calculator", "pkg")
      self.assertContainsAll(result, expected)
      print(result)

    def test_bin_directory_outside_working_directory(self):
      expected = "Result for '/bin' directory:\n" + '    Error: Cannot list "/bin" as it is outside the permitted working directory'
      result = get_files_info("calculator", "/bin")
      self.assertEqual(result, expected)
      print(result)

    def test_parent_directory_outside_working_directory(self):
      expected = "Result for '../' directory:\n" + '    Error: Cannot list "../" as it is outside the permitted working directory'
      result = get_files_info("calculator", "../")
      self.assertEqual(result, expected)
      print(result)

if __name__ == "__main__":
  unittest.main()
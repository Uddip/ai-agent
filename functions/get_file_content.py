import os
from os.path import isfile

def get_file_info(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not absolute_path.startswith(os.path.abspath(working_directory)):
            raise Exception(f"Cannot read \"{file+path}\" as it is outside the permitted working directory")

        if not is.path.isfile(absolute_path):
            raise Exception(f"File not found or if not a regular file: \"{file_path}\" ")

    except Exception as e:
        return str(f"Error: {e}")

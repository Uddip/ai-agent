import os

def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not absolute_path.startswith(os.path.abspath(working_directory)):
            raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    except Exception as e:
        return str(f"Error: {e}")


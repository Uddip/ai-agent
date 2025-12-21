import os

def write_file(working_directory, file_path, content):
    try:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_path = os.path.abspath(working_directory)

        if not abs_file_path.startswith(working_directory_path):
            raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')

        if os.path.isdir(abs_file_path):
            return f'Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return str(f"Error: {e}")


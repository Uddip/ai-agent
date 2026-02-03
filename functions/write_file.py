import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating directories as needed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
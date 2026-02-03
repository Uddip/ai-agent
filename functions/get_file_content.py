import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            raise Exception(f"Cannot read \"{file_path}\" as it is outside the permitted working directory")

        if not os.path.isfile(abs_file_path):
            raise Exception(f'File not found or is not a regular file: "{file_path}" ')

        with open(abs_file_path, "r") as file:
            file_content = file.read(MAX_CHARS)
            if file.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content

    except Exception as e:
        return str(f"Error: {e}")
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory, up to a maximum character limit",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


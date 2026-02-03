import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)

        if not abs_file_path.startswith(abs_working_dir):
            raise Exception(f'Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.exists(abs_file_path):
            raise Exception(f'File "{file_path}" does not exist or is not a regular file')

        if not abs_file_path.endswith('.py'):
            raise Exception(f'"{file_path}" is not a Python file.')

        command = ['python', abs_file_path]
        if args:
            command.extend(args)

        completed_process = subprocess.run(command, cwd=abs_working_dir, timeout=30, capture_output=True, text=True)

        output = []
        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode}"

        if not completed_process.stdout and not completed_process.stderr:
            output.append("No output produced")

        if completed_process.stdout:
            output.append(f"STDOUT:\n{completed_process.stdout}")

        if completed_process.stderr:
            output.append(f"STDERR:\n{completed_process.stderr}")

        return "\n".join(output)

    except Exception as e:
        return str(f"Error: executing Python file: {e}")

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(
                        type=types.Type.STRING,
                    ),
                    description="List of arguments to pass to the Python script",
                ),
        },
        required=["file_path"],
    ),
)

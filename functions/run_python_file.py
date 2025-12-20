import os
import subprocess

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

        completed_process = subprocess.run(['python', abs_file_path, *args], timeout=30, capture_output=True, text=True)

        if not completed_process:
            return f'No output produced'

        output = f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

        if not completed_process.returncode == 0:
            output += f"\nProcess exited with code {completed_process.returncode}"

        return output

    except Exception as e:
        return str(f"Error: executing Python file: {e}")



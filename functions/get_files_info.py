import os

def get_files_info(working_directory, directory="."):
  absolute_path = os.path.abspath(os.path.join(working_directory, directory))

  if not absolute_path.startswith(os.path.abspath(working_directory) + os.sep):
    raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
  
  if not os.path.isdir(directory):
    raise Exception(f'Error: "{directory}" is not a directory')
  
  report = []

  file = os.path.join(absolute_path, "README.md")
  report.append(f"README.md: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}")

  file = os.path.join(absolute_path, "src")
  report.append(f"src: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}")

  file = os.path.join(absolute_path, "package.json")
  report.append(f"package.json: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}")

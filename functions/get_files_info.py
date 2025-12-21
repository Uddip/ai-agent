import os

def get_files_info(working_directory, directory="."):
  try:
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

    if not target_dir.startswith(abs_working_dir):
      raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(target_dir):
      raise Exception(f'"{directory}" is not a directory')

    report = []

    for file_name in os.listdir(target_dir):
      file_path = os.path.join(target_dir, file_name)
      report.append(f" - {file_name}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    
    return "\n".join(report)
  
  except Exception as e:
    return f"Error listing files: Error: {e}"
